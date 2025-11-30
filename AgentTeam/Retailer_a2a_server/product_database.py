import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "products.sqlite")

# ------------------------------------------------------------
# Create database + tables
# ------------------------------------------------------------
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        name TEXT,
        brand TEXT,
        price INTEGER,
        rating REAL,
        features TEXT,
        retailer TEXT
    )
    """)

    conn.commit()
    conn.close()


# ------------------------------------------------------------
# Insert ONE product
# ------------------------------------------------------------
def insert_product(category, name, brand, price, rating, features, retailer):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO products (category, name, brand, price, rating, features, retailer)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        category.lower(),
        name,
        brand,
        price,
        rating,
        ",".join(features) if isinstance(features, list) else features,
        retailer
    ))

    conn.commit()
    conn.close()


# ------------------------------------------------------------
# Insert MANY products at once
# ------------------------------------------------------------
def bulk_insert(category, product_list):
    for p in product_list:
        insert_product(
            category=category,
            name=p["name"],
            brand=p["brand"],
            price=p["price"],
            rating=p["rating"],
            features=p.get("features", []),
            retailer=p["retailer"]
        )


# ------------------------------------------------------------
# Fetch products by category (used by retailer agent)
# ------------------------------------------------------------
def fetch_products_by_category(category: str):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        SELECT name, brand, price, rating, features, retailer
        FROM products
        WHERE category = ?
    """, (category.lower(),))

    rows = cur.fetchall()
    conn.close()

    products = []
    for r in rows:
        products.append({
            "name": r[0],
            "brand": r[1],
            "price": r[2],
            "rating": r[3],
            "features": r[4].split(",") if r[4] else [],
            "retailer": r[5]
        })

    return products


# ------------------------------------------------------------
# INITIAL DATA SEEDING (loads your old mock PRODUCT_DB automatically)
# ------------------------------------------------------------
def seed_if_empty():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM products")
    count = cur.fetchone()[0]
    conn.close()

    if count > 0:
        print("[SQLite] Product database already initialized.")
        return

    print("[SQLite] Seeding initial product data...")

    # Your original PRODUCT_DB mock data
    PRODUCT_DB = {
        "earbuds": [
            {"name": "boAt Airdopes 141", "brand": "boAt", "price": 1299, "rating": 4.2,
             "features": ["wireless", "fast charging"], "retailer": "Amazon"},
            {"name": "boAt Airdopes 141", "brand": "boAt", "price": 1199, "rating": 4.1,
             "features": ["wireless"], "retailer": "Flipkart"},
            {"name": "boAt Airdopes 190", "brand": "boAt", "price": 1599, "rating": 4.3,
             "features": ["gaming", "low latency", "wireless"], "retailer": "Amazon"},
            {"name": "boAt Airdopes 441", "brand": "boAt", "price": 1999, "rating": 4.0,
             "features": ["wireless", "water resistant"], "retailer": "Croma"},
            {"name": "Samsung Galaxy Buds Pro", "brand": "Samsung", "price": 10999, "rating": 4.6,
             "features": ["wireless", "noise cancellation", "water resistant"], "retailer": "Amazon"},
            {"name": "Apple AirPods Pro", "brand": "Apple", "price": 24999, "rating": 4.7,
             "features": ["wireless", "noise cancellation", "bluetooth"], "retailer": "Flipkart"},
            {"name": "OnePlus Buds Z2", "brand": "OnePlus", "price": 3999, "rating": 4.3,
             "features": ["wireless", "noise cancellation", "fast charging"], "retailer": "Amazon"}
        ],
        "phones": [
            {"name": "iPhone 14", "brand": "Apple", "price": 69999, "rating": 4.8,
             "features": ["oled", "5g", "a15 chip"], "retailer": "Amazon"},
            {"name": "iPhone 14", "brand": "Apple", "price": 67999, "rating": 4.7,
             "features": ["5g", "face id"], "retailer": "Flipkart"},
            {"name": "iPhone 13", "brand": "Apple", "price": 58999, "rating": 4.6,
             "features": ["5g", "dual camera"], "retailer": "Croma"},
            {"name": "iPhone 15", "brand": "Apple", "price": 79999, "rating": 4.9,
             "features": ["usb-c", "a16 chip", "5g"], "retailer": "Reliance Digital"},
            {"name": "Samsung Galaxy S23", "brand": "Samsung", "price": 74999, "rating": 4.8,
             "features": ["snapdragon 8 gen 2", "amoled", "5g"], "retailer": "Amazon"},
            {"name": "Samsung Galaxy A54", "brand": "Samsung", "price": 37999, "rating": 4.4,
             "features": ["amoled", "5g", "water resistance"], "retailer": "Flipkart"},
            {"name": "OnePlus 11R", "brand": "OnePlus", "price": 38999, "rating": 4.6,
             "features": ["snapdragon 8+ gen 1", "5g"], "retailer": "Amazon"},
            {"name": "OnePlus Nord CE 3", "brand": "OnePlus", "price": 24999, "rating": 4.3,
             "features": ["amoled", "5g"], "retailer": "Croma"},
        ]
    }

    # Insert all categories
    for category, items in PRODUCT_DB.items():
        bulk_insert(category, items)

    print("[SQLite] Product DB seeded successfully!")


# ------------------------------------------------------------
# Initialize + Seed (auto-run)
# ------------------------------------------------------------
init_db()
seed_if_empty()
