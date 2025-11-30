import os
import asyncio
from typing import List
from google.adk.agents.llm_agent import LlmAgent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types
from google.adk.models.google_llm import Gemini
from pydantic import BaseModel
from typing import Optional
from google.adk.agents.remote_a2a_agent import AGENT_CARD_WELL_KNOWN_PATH
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent
from tool import compare_products
from tool import Product, Preferences, Constraints
from google.adk.runners import InMemoryRunner
from google.adk.plugins.logging_plugin import (
    LoggingPlugin,
)
os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")
retry_config = types.HttpRetryOptions(
    attempts=5,  
    exp_base=7,  
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504], 
)
retailer_agent = RemoteA2aAgent(
    name="retailer_agent",
    description="Remote Retailer Agent that fetches product data.",
    agent_card=(
        f"http://localhost:8001{AGENT_CARD_WELL_KNOWN_PATH}"
    ),
)
root_agent= LlmAgent(
    model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
    name="root_agent",
    description="Local orchestrator agent.It always delegates product-related queries to retailer_agent. retailer_agent returns products information to this agent",
    instruction="""
    ->You should Obey The following three rules And all these three rules Represents three different scenarios you might encounter While interacting with user, One more thing you might also encounter some other scenarios Handle those Intelligently:
        1.when the user ask to list products(example:- List down all the phones under 70,000 ,List down all the T shirts under 600, Show me all the available options of Jeans etc)in that case you must call retailer_agent and forward user's request and also keep in mind If the user has asked only for the list of products,Not explicitly asked for the comparison of those products,To find out the best product,you must not call The tool compare_products and After getting back That From retailer_agent you should show that list to user.
        
        2.User can also ask for Specific products to compare And those products wil be From the list You had provided to the user earlier,In this case Along with those specific products details(along with other details Apply user preferences(brand,features) and constraints(max price,min rating)) You must call The tool compare_products and then return result to user.
            examples:-
                ->From the list of atta Compare and find The best one among 2nd,3rd and 4th option.
            [IMPORTANT]If the user just say something like"Suggest the best one Among the first and the fifth option" Then in this types of scenario You should always consider The last list of products you had provided to the user)
        
        3.User can also directly ask for Comparison and finding best one according to user's need,In this case You must Delegate That query to retailer_agent And after getting back the result(list of proucts) from the retailer_agent,You will Call 
        the tool compare_products With those specific products(Basically these are the products which Falls under Criteria Mentioned by the user,for example Find best product With rating 4.4 then Here rating is the criteria, 
        Suggest the best Possible product With features Noise cancellation,wifi Here features is the criteria) along with their essential details like If the user has mentioned about any brand,Features,Budget, Minimum rating requirement.
        And then show that best product to user and along with that you will also show that 
        list Using which your compare_products Tool did comparison.
            examples: ->Compare and find best earbuds under 25,000.
                      ->Suggest best saree of brand Anouk My budget is 2000
    
    
    ->Do NOT ask the user to provide the list of products.  
      The retailer_agent is responsible for fetching products from the database and return back those products and their details to you.
      Remember it is your responsibility to interact with user.
    """,
   tools=[compare_products],
   sub_agents=[retailer_agent]
)
session_service = InMemorySessionService()
APP_NAME = "shopping_app"
USER_ID = "user_1"
SESSION_ID = "session_001"
async def init_session(app_name:str,user_id:str,session_id:str) -> InMemorySessionService:
     session = await session_service.create_session(
         app_name=app_name,
         user_id=user_id,
         session_id=session_id
     )
     print(f"Session created: App='{app_name}', User='{user_id}', Session='{session_id}'")
     return session
 
session = asyncio.run(init_session(APP_NAME,USER_ID,SESSION_ID))
runner_observibility = InMemoryRunner(
    agent=root_agent,
    plugins=[
        LoggingPlugin()
    ]
)
runner = Runner(
    agent=root_agent, 
    app_name=APP_NAME,   
    session_service=session_service 
)
async def call_agent_async(query: str, runner, user_id, session_id):
  """Sends a query to the agent and prints the final response."""
  print(f"\n>>> User Query: {query}")
  content = types.Content(role='user', parts=[types.Part(text=query)])
  final_response_text = "Agent did not produce a final response." # Default
  async for event in runner.run_async(user_id=user_id, session_id=session_id, new_message=content):
      # You can uncomment the line below to see *all* events during execution
      # print(f"  [Event] Author: {event.author}, Type: {type(event).__name__}, Final: {event.is_final_response()}, Content: {event.content}")
      if event.is_final_response():
          if event.content and event.content.parts:
             # Assuming text response in the first part
             final_response_text = event.content.parts[0].text
          elif event.actions and event.actions.escalate: # Handle potential errors/escalations
             final_response_text = f"Agent escalated: {event.error_message or 'No specific message.'}"
          # Add more checks here if needed (e.g., specific error codes)
          break # Stop processing events once the final response is found

  print(f"<<< Agent Response: {final_response_text}")

async def run_conversation():
    print("Welcome to the shopping Bot,when you are done with your shopping type any one of these exit,quit,bye")
    while True:
        print("enter your input")
        user_query = input("You: ")
        if user_query.lower() in ["exit", "quit", "bye"]:
            print("shopping Bot: Goodbye!")
            break
        await call_agent_async(user_query, runner=runner, user_id=USER_ID, session_id=SESSION_ID)
    print("enter your input for comprehensive logs,when you want to discontinue type any one of these exit,quit,bye")
    while True:
        test_query = input("You: ")
        if test_query.lower() in ["exit", "quit", "bye"]:
            print("goodbye")
            break
        await runner_observibility.run_debug(test_query)

if __name__ == "__main__":
    try:
        asyncio.run(run_conversation())
    except Exception as e:
        print(f"An error occurred: {e}")
