# PROBLEM:-

Consumers often spend a significant amount of time jumping between different online retailers when trying to find the best product that fits their specific requirements.
Prices vary across platforms, product listings can be overwhelming, and there is no unified way to compare quality, price, and user preference simultaneously.
This leads to:
* Wasted time browsing multiple sites
* Higher chances of paying more for the same product elsewhere
* Difficulty identifying the best match among many similar options
A system capable of searching across platforms, extracting the relevant product details, and selecting the best product automatically would save both time and money for users.
My project addresses this by using a chain of AI agents that takes a user’s product query and returns the optimal product from a list of retailers—fully autonomously.

# SOLUTION:-

Here is the workflow of how the system behaves during a real usage scenario:

A. Scenario 1:- 
1. The user inputs a request like:
   “Find the best budget smartphones under 300 with rating of 4.5.”
2. The root_Agent receives the query and forwards it to the retailer_Agent.
3. The Retailer_Agent searches its SQLite product database and returns a list of matching smartphones to root_agent, each with attributes such as:           
   * Name
   * Retailer
   * Price
   * featres
   * User ratings
4 The Root_agent then using tool compare_products scores each product and selects the best one based on the user’s priorities.
5 The final result is returned to the user by the root_agent, something like:
   “The best option is X because it offers the optimal balance of price, battery life, and overall value.”

Even with a simple SQLite backend, this demonstrates how powerful agent collaboration can be. Once connected to retailer APIs, this can operate in real time and handle thousands of products instantly.

B. Scenario 2:-
1. The user inputs a request like:
   " Show me all available Shirt Under 2000"
2.The root_Agent receives the query and forwards it to the retailer_Agent.
3.The Retailer_Agent searches its SQLite product database and returns a list of matching shirts to root_agent, each with attributes such as:           
   *Name
   *Retailer
   *Price
   *featres
   *User ratings
4. Now the root_agent will show that list to the user.
5. Now the user may asks to compare First and the fifth option of products from that list.
6. Root_agent using compare_products will compare only these two products According to the users need and find the best 1 and return it to the user


# ARCHITECTURE:-

This project has in total has two agents one is local And another one is remote. The Ai agent named root_agent And the remote ai agent named retailer_agent.The root_agent is responsible for interacting with the user,The root_agent will receive the user's query and send that query To the retailer_agent So that it Fetch all the matching products according to the Need of the query And return back all the matching products along with their details To the root_agent via a A2A.when the retailer_agent recieves The queries From root_agent the retailer_agent then use a custom tool named get_product_details For fetching Matching products list From its database that is here sqlite database. After receiving that list of products From the retailer_agent the Root_agent Can also use a custom tool named compare_products For comparing and finding the best possible product according to the user's need Like if the user has mentioned for a specific brand or user has some constraint regarding budget or user wants high rating products and all these cases will be considered Using this specific tool compare_products And after getting That best product The root agent will return or show That product to the user. The root_agent is also stateful that means it can remember What were the products Asked by the user And therefore From a previously delivered list of products An user can choose Any number of products To be compared for getting the best possible among them. For observability purpose built-in LoggingPlugin (that automatically captures all agent activity) has been incorporated.

summary:-
1. two LLMAgents
2. two LLMAgents are connected via A2A protocol
3. root_agent has custom tool compare_products
   retailer_agent has custom tool get_product_details
4. root_agent is stateful(inmemorysessionservice)
5. built-in LoggingPlugin

# SETUP INSTRUCTIONS:-

1. Download and install Anaconda
2. create an GOOGLE Gemini API key in Google AI Studio.
3. Open a folder in vs code and navigate to that
4. Clone the repository:-
    git clone https://github.com/Sayan-Sasmal/Shopping-Assistant.git
5. Create virtual environment:-
    conda create -
    p ./venv python=3.13.5 
6. Activate virtual environment:
    conda activate ./venv
7. Now run:-
   pip install google-adk[a2a]
8. Run the remote retailer agent(Retailer_a2a_server) :-
   1. uvicorn AgentTeam.Retailer_a2a_server.agent:a2a_app --host localhost --port 8001
   2. verify agent card:-
        open this url:-http://localhost:8001/.well-known/agent-card.json
9. Open another terminal(cmd):-
    1. run cd AgentTeam
    2. run python root_agent.py
10. Now start interacting with the agent.

# IMPORTANT NOTE:-
  For this project Only the following list of keywords Can be used to search Products And compare them:-
  keywords:-laptops,smartwatches,shirt,saree,atta,lehenga,rice,paneer,jeans,helmet,sugar,tea,coffee,operating_system_book,engineering_mathematics_book,nvidia_geforce_rtx_gpu,ram
   example:1." What are the available options of operating_system_book From the retailer Flipkart"
           2." From the list of paneer Compare and find the best one among first and the 5th option"