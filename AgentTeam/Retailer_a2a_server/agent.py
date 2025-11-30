import os
from google.adk.agents.llm_agent import LlmAgent
from google.genai import types
from google.adk.models.google_llm import Gemini
from google.adk.a2a.utils.agent_to_a2a import to_a2a
from pydantic import BaseModel
from typing import Optional
from typing import List
from .product_database import fetch_products_by_category

os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")

class Product(BaseModel):
    name: str
    brand: str
    price: int
    rating: float
    features: Optional[List[str]] = None
    retailer: Optional[str] = None

class Preferences(BaseModel):
    brand: Optional[str] = None
    features: Optional[List[str]] = None

class Constraints(BaseModel):
    max_price: Optional[int] = None
    min_rating: Optional[float] = None
def get_product_details(product_name: str) -> List[Product]:
    """
    Tool: get_product_details
    Description:
        Returns static product details from multiple retailers without using
        any external scraping. This acts as a mock product database.

    Args:
        product_name (str): Name of the product user is looking for.
            Example: "sony headphones"

    Returns:
        list: A list of product dictionaries, each representing a retailer's listing.
    """
    category = product_name.lower().strip()

    raw_products = fetch_products_by_category(category)
    print("\n=== RETAILER_AGENT: PRODUCTS FETCHED FROM PRODUCT_DB ===")
    print("Query:", product_name)
    print("Count:", len(raw_products))
    for p in raw_products:
        print(" → ", p)
    return [Product(**p) for p in raw_products]
#TARGET_FOLDER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mcpspace")
retry_config = types.HttpRetryOptions(
    attempts=5,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],  # Retry on these HTTP errors
)
root_agent = LlmAgent(
    model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
    name='Retailer_agent',
    description="Retailer product agent that fetches products from PRODUCT_DB and, it can show list of all matching products",
    instruction="""
    You are the retailer agent.Your job is to fetch products from PRODUCT_DB.
    rule:
    1.you will never interact with user.you will always interact with root_agent.
    2. You should always remember This list of keywords:[laptops,smartwatches,shirt,saree,atta,lehenga,rice,paneer,jeans,helmet,sugar,tea,coffee,operating_system_book,engineering_mathematics_book,nvidia_geforce_rtx_gpu,ram], 
       You should look in the query Which keyword have been given in that query Among all these keywords mentioned in this list,
       Keywords may not always be Written directly Like For example If root_agent queries "List down all the available organic Paneer" You should 
       choose "Paneer" as the keyword Not "organic paneer" If asked " Show all Men's shirt" Then choose keyword "Shirt",You must be intelligent enough To Figure out what is the keyword that you can use for matching Intelligently.
       Always fetch ALL matching products using get_product_details.
    3. If root_agent asks for "list"(Example:-List all the product Under 5000, List all Products from brand a(example:-ASUS) and brand b(example:-samsung)), "show all", "all options", or anything similar:
       → Return ALL fetched products directly to root_agent not to user.
    5. NEVER ask the user for product lists. You must fetch products yourself.
    """,
    tools=[get_product_details]
)
a2a_app = to_a2a(root_agent, port=8001)

