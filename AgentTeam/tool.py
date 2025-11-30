from typing import Optional
from pydantic import BaseModel
from typing import List
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
def compare_products(
    products: List[Product],
    preferences: Optional[Preferences] = None,
    constraints: Optional[Constraints] = None
) -> Optional[Product]:
    """
    Tool: compare_products
    Description:
        Compares multiple products and returns the best option based on user
        preferences (brand, features, etc.) and constraints (max budget, min rating).

    Args:
        products (list): List of product dictionaries.
        preferences (dict): User preferences. Example:
            {
                "brand": "Sony",
                "features": ["noise cancellation", "wireless"]
            }
        constraints (dict): User constraints. Example:
            {
                "max_price": 30000,
                "min_rating": 4.5
            }

    Returns:
        dict: Best product match or None if no product fits criteria.
    """
    print("\n=== DEBUG: products received by comparator ===")
    for idx, p in enumerate(products):
        print(f"{idx}: {type(p)} → {p}")
    # Convert dicts → typed Product models
    products = [Product(**p) if isinstance(p, dict) else p for p in products]

    if isinstance(preferences, dict):
        preferences = Preferences(**preferences)

    if isinstance(constraints, dict):
        constraints = Constraints(**constraints)

    if not products:
        return None

    max_price = constraints.max_price if constraints else None
    min_rating = constraints.min_rating if constraints else None
    
    preferred_brand = preferences.brand if preferences else None
    preferred_features = set(preferences.features or []) if preferences else set()

    # Step 1 — Filter by constraints
    filtered = []
    for p in products:
        if max_price and p.price > max_price:
            continue
        if min_rating and p.rating < min_rating:
            continue
        filtered.append(p)

    if not filtered:
        return None

    # Step 2 — Score products based on preferences
    def score(product: Product):
        score = 0

        # Brand preference (boost score)
        if preferred_brand and product.brand.lower() == preferred_brand.lower():
            score += 3

        # Feature matching
        product_features = set(product.features or [])
        score += len(product_features & preferred_features)

        # Rating contribution
        score += product.rating * 0.5

        # Price advantage (lower is better)
        score += (1 / product.price) * 1000  # Normalized weight

        return score

    # Step 3 — Pick best scoring product
    best = max(filtered, key=score)
    #best["_score"] = score(best)  # For debugging

    return best