# insert.py
from product_database import bulk_insert

def seed_custom_products():

    # ---------------------------------------------------------
    #  LAPTOPS (7 products)
    # ---------------------------------------------------------
    bulk_insert("laptops", [
        {"name": "MacBook Air M2", "brand": "Apple", "price": 99999, "rating": 4.9,
         "features": ["m2 chip", "retina"], "retailer": "Amazon"},
        {"name": "Dell XPS 13", "brand": "Dell", "price": 119999, "rating": 4.7,
         "features": ["touchscreen"], "retailer": "Amazon"},
        {"name": "HP Victus 16", "brand": "HP", "price": 79999, "rating": 4.5,
         "features": ["gaming", "144hz"], "retailer": "Amazon"},
        {"name": "Lenovo ThinkPad X1 Carbon", "brand": "Lenovo", "price": 139999, "rating": 4.8,
         "features": ["lightweight", "premium build"], "retailer": "Amazon"},
        {"name": "Acer Aspire 5", "brand": "Acer", "price": 42999, "rating": 4.2,
         "features": ["i5", "ssd"], "retailer": "Amazon"},
        {"name": "Asus TUF Gaming F15", "brand": "Asus", "price": 85999, "rating": 4.6,
         "features": ["rtx 3050", "144hz"], "retailer": "Flipkart"},
        {"name": "Samsung Galaxy Book 3", "brand": "Samsung", "price": 88999, "rating": 4.6,
         "features": ["amoled display"], "retailer": "Amazon"},
    ])

    # ---------------------------------------------------------
    #  SMARTWATCHES (7 products)
    # ---------------------------------------------------------
    bulk_insert("smartwatches", [
        {"name": "Apple Watch Series 9", "brand": "Apple", "price": 41999, "rating": 4.8,
         "features": ["ecg", "amoled"], "retailer": "Apple Store"},
        {"name": "Samsung Galaxy Watch 6", "brand": "Samsung", "price": 32999, "rating": 4.7,
         "features": ["health tracking"], "retailer": "Amazon"},
        {"name": "Fitbit Sense 2", "brand": "Fitbit", "price": 28999, "rating": 4.5,
         "features": ["stress monitor"], "retailer": "Amazon"},
        {"name": "Garmin Venu 2", "brand": "Garmin", "price": 37999, "rating": 4.7,
         "features": ["gps tracking"], "retailer": "Amazon"},
        {"name": "Amazfit GTR 4", "brand": "Amazfit", "price": 16999, "rating": 4.5,
         "features": ["amoled"], "retailer": "Amazon"},
        {"name": "Noise ColorFit Pro 4", "brand": "Noise", "price": 2999, "rating": 4.1,
         "features": ["bluetooth calling"], "retailer": "Amazon"},
        {"name": "OnePlus Watch 2", "brand": "OnePlus", "price": 24999, "rating": 4.6,
         "features": ["dual OS"], "retailer": "Amazon"},
    ])
    bulk_insert("shirt", [
    {"name": "Men's Cotton Casual Shirt", "brand": "Peter England", "price": 1199, "rating": 4.3,
     "features": ["cotton", "regular fit"], "retailer": "Amazon"},

    {"name": "Men's Slim Fit Formal Shirt", "brand": "Arrow", "price": 1499, "rating": 4.4,
     "features": ["formal wear", "slim fit"], "retailer": "Flipkart"},

    {"name": "Men's Checked Casual Shirt", "brand": "Highlander", "price": 799, "rating": 4.2,
     "features": ["checked pattern", "cotton blend"], "retailer": "Amazon"},

    {"name": "Men's Linen Shirt", "brand": "Raymond", "price": 1999, "rating": 4.5,
     "features": ["linen", "breathable"], "retailer": "Amazon"},

    {"name": "Men's Denim Shirt", "brand": "Levi's", "price": 2499, "rating": 4.4,
     "features": ["denim", "stylish design"], "retailer": "Flipkart"},

    {"name": "Men's Mandarin Collar Shirt", "brand": "Roadster", "price": 999, "rating": 4.1,
     "features": ["mandarin collar", "casual"], "retailer": "Myntra"},

    {"name": "Men's Party Wear Shirt", "brand": "Louis Philippe", "price": 2799, "rating": 4.6,
     "features": ["premium fabric", "party wear"], "retailer": "Amazon"},
])

bulk_insert("saree", [
    {"name": "Banarasi Silk Saree", "brand": "Kanjivaram", "price": 3499, "rating": 4.6,
     "features": ["silk", "traditional"], "retailer": "Amazon"},

    {"name": "Cotton Printed Saree", "brand": "Sangria", "price": 899, "rating": 4.3,
     "features": ["cotton", "printed"], "retailer": "Flipkart"},

    {"name": "Georgette Designer Saree", "brand": "Anouk", "price": 1599, "rating": 4.4,
     "features": ["georgette", "designer"], "retailer": "Myntra"},

    {"name": "Chiffon Embroidered Saree", "brand": "Ritu Kumar", "price": 2999, "rating": 4.5,
     "features": ["chiffon", "embroidered"], "retailer": "Amazon"},

    {"name": "Kalamkari Art Saree", "brand": "FabIndia", "price": 2299, "rating": 4.4,
     "features": ["handcrafted", "art print"], "retailer": "FabIndia Store"},

    {"name": "Silk Blend Saree", "brand": "Vark", "price": 1899, "rating": 4.3,
     "features": ["silk blend", "lightweight"], "retailer": "Myntra"},

    {"name": "Party Wear Net Saree", "brand": "Satrani", "price": 1299, "rating": 4.2,
     "features": ["net", "party wear"], "retailer": "Flipkart"},
])

bulk_insert("atta", [
    {"name": "Aashirvaad Shudh Chakki Atta 10kg", "brand": "Aashirvaad", "price": 449, "rating": 4.6,
     "features": ["whole wheat", "chakki ground"], "retailer": "Amazon"},

    {"name": "Fortune Whole Wheat Atta 10kg", "brand": "Fortune", "price": 429, "rating": 4.4,
     "features": ["100% wheat"], "retailer": "Flipkart"},

    {"name": "Patanjali Whole Wheat Atta 10kg", "brand": "Patanjali", "price": 399, "rating": 4.5,
     "features": ["stone ground"], "retailer": "Amazon"},

    {"name": "Tata Sampann Atta 10kg", "brand": "Tata", "price": 459, "rating": 4.5,
     "features": ["nutrient rich"], "retailer": "Amazon"},

    {"name": "Annapurna Atta 10kg", "brand": "Annapurna", "price": 419, "rating": 4.3,
     "features": ["soft rotis"], "retailer": "Flipkart"},

    {"name": "Nature Fresh Sampoorna Atta 10kg", "brand": "Nature Fresh", "price": 439, "rating": 4.4,
     "features": ["natural wheat"], "retailer": "Amazon"},

    {"name": "Rajdhani Chakki Atta 10kg", "brand": "Rajdhani", "price": 389, "rating": 4.2,
     "features": ["traditional grinding"], "retailer": "Flipkart"},
])
bulk_insert("lehenga", [
    {"name": "Embroidered Bridal Lehenga", "brand": "Sabyasachi", "price": 49999, "rating": 4.8,
     "features": ["heavy embroidery", "silk fabric", "size: free size"], "retailer": "Amazon"},

    {"name": "Georgette Party Wear Lehenga", "brand": "Biba", "price": 5999, "rating": 4.5,
     "features": ["georgette", "lightweight", "size: S-XL"], "retailer": "Flipkart"},

    {"name": "Printed Festive Lehenga", "brand": "W for Women", "price": 3499, "rating": 4.3,
     "features": ["printed design", "cotton blend", "size: S-L"], "retailer": "Myntra"},

    {"name": "Net Designer Lehenga", "brand": "Satrani", "price": 4299, "rating": 4.4,
     "features": ["net fabric", "embroidered", "size: M-XXL"], "retailer": "Amazon"},

    {"name": "Banarasi Silk Lehenga", "brand": "Kalki Fashion", "price": 8999, "rating": 4.6,
     "features": ["banarasi silk", "traditional", "size: free size"], "retailer": "Amazon"},

    {"name": "Sequins Party Lehenga", "brand": "Zara Designers", "price": 5599, "rating": 4.2,
     "features": ["sequins work", "modern design", "size: XS-L"], "retailer": "Flipkart"},

    {"name": "Velvet Heavy Lehenga", "brand": "House of Masaba", "price": 14999, "rating": 4.7,
     "features": ["velvet", "premium embroidery", "size: free size"], "retailer": "Amazon"},
])

bulk_insert("rice", [
    {"name": "Basmati Rice 5kg", "brand": "India Gate", "price": 599, "rating": 4.6,
     "features": ["long grain", "aromatic"], "retailer": "Amazon"},

    {"name": "Sona Masoori Rice 10kg", "brand": "24 Mantra", "price": 679, "rating": 4.4,
     "features": ["organic", "lightweight"], "retailer": "Flipkart"},

    {"name": "Kolam Rice 5kg", "brand": "Fortune", "price": 399, "rating": 4.3,
     "features": ["soft texture"], "retailer": "Amazon"},

    {"name": "Brown Rice 1kg", "brand": "Daawat", "price": 149, "rating": 4.4,
     "features": ["healthy", "fiber rich"], "retailer": "Amazon"},

    {"name": "Kolam HMT Rice 10kg", "brand": "Tata Sampann", "price": 799, "rating": 4.5,
     "features": ["premium quality"], "retailer": "Flipkart"},

    {"name": "Idli Rice 5kg", "brand": "Patanjali", "price": 449, "rating": 4.2,
     "features": ["specially for idli/dosa"], "retailer": "Amazon"},

    {"name": "Jeera Samba Rice 5kg", "brand": "Annapurna", "price": 499, "rating": 4.3,
     "features": ["fragrant"], "retailer": "Amazon"},
])

bulk_insert("paneer", [
    {"name": "Fresh Paneer 200g", "brand": "Amul", "price": 85, "rating": 4.6,
     "features": ["fresh dairy"], "retailer": "Amazon"},

    {"name": "Organic Paneer 200g", "brand": "Milky Mist", "price": 95, "rating": 4.5,
     "features": ["organic"], "retailer": "Flipkart"},

    {"name": "Premium Malai Paneer 200g", "brand": "Haldiram's", "price": 89, "rating": 4.4,
     "features": ["creamy texture"], "retailer": "Amazon"},

    {"name": "Soft Paneer 200g", "brand": "Mother Dairy", "price": 82, "rating": 4.5,
     "features": ["soft"], "retailer": "Amazon"},

    {"name": "High Protein Paneer 200g", "brand": "Patanjali", "price": 75, "rating": 4.3,
     "features": ["high protein"], "retailer": "Flipkart"},

    {"name": "Fresh Cottage Cheese 200g", "brand": "Verka", "price": 78, "rating": 4.2,
     "features": ["fresh"], "retailer": "Amazon"},

    {"name": "Premium Paneer 200g", "brand": "Gowardhan", "price": 90, "rating": 4.4,
     "features": ["rich taste"], "retailer": "Flipkart"},
])

bulk_insert("jeans", [
    {"name": "Men's Slim Fit Jeans", "brand": "Levi's", "price": 2599, "rating": 4.5,
     "features": ["denim", "stretchable", "size: 30-38"], "retailer": "Amazon"},

    {"name": "Men's Regular Fit Jeans", "brand": "Wrangler", "price": 1999, "rating": 4.4,
     "features": ["regular fit", "durable", "size: 28-40"], "retailer": "Flipkart"},

    {"name": "Men's Skinny Fit Jeans", "brand": "Roadster", "price": 1299, "rating": 4.2,
     "features": ["skinny", "faded look", "size: 30-36"], "retailer": "Myntra"},

    {"name": "Women's High-Rise Jeans", "brand": "Only", "price": 2499, "rating": 4.6,
     "features": ["high-rise", "stretchable", "size: 26-34"], "retailer": "Flipkart"},

    {"name": "Women's Mom Fit Jeans", "brand": "H&M", "price": 2299, "rating": 4.4,
     "features": ["relaxed fit", "soft denim", "size: 26-32"], "retailer": "H&M Store"},

    {"name": "Women's Straight Fit Jeans", "brand": "Pepe Jeans", "price": 2599, "rating": 4.5,
     "features": ["straight fit", "premium denim", "size: 28-36"], "retailer": "Amazon"},

    {"name": "Men's Tapered Fit Jeans", "brand": "Lee", "price": 2199, "rating": 4.3,
     "features": ["tapered", "flex denim", "size: 30-38"], "retailer": "Flipkart"},
])

bulk_insert("helmet", [
    {"name": "Full Face Helmet", "brand": "Steelbird", "price": 1599, "rating": 4.5,
     "features": ["ISI certified", "scratch resistant"], "retailer": "Amazon"},

    {"name": "Open Face Helmet", "brand": "Vega", "price": 1299, "rating": 4.4,
     "features": ["ventilation"], "retailer": "Flipkart"},

    {"name": "Sports Bike Helmet", "brand": "Axor", "price": 3999, "rating": 4.6,
     "features": ["aerodynamic", "double visor"], "retailer": "Amazon"},

    {"name": "Modular Helmet", "brand": "Studds", "price": 2999, "rating": 4.5,
     "features": ["flip-up", "ISI"], "retailer": "Amazon"},

    {"name": "Racing Helmet", "brand": "LS2", "price": 8499, "rating": 4.7,
     "features": ["lightweight", "ABS shell"], "retailer": "Amazon"},

    {"name": "Urban Riding Helmet", "brand": "Gliders", "price": 999, "rating": 4.2,
     "features": ["stylish"], "retailer": "Flipkart"},

    {"name": "Adventure Helmet", "brand": "Royal Enfield", "price": 3999, "rating": 4.5,
     "features": ["off-road design"], "retailer": "Amazon"},
])

bulk_insert("sugar", [
    {"name": "Refined Sugar 5kg", "brand": "Madhur", "price": 245, "rating": 4.5,
     "features": ["refined"], "retailer": "Amazon"},

    {"name": "Brown Sugar 1kg", "brand": "Tata", "price": 75, "rating": 4.4,
     "features": ["organic"], "retailer": "Flipkart"},

    {"name": "Sulphur Free Sugar 5kg", "brand": "Dhampur", "price": 255, "rating": 4.6,
     "features": ["sulphur free"], "retailer": "Amazon"},

    {"name": "Organic Cane Sugar 1kg", "brand": "24 Mantra", "price": 95, "rating": 4.3,
     "features": ["unrefined"], "retailer": "Amazon"},

    {"name": "Premium Sugar 5kg", "brand": "Parry's", "price": 265, "rating": 4.4,
     "features": ["premium"], "retailer": "Flipkart"},

    {"name": "Jaggery Powder 1kg", "brand": "BB Royal", "price": 89, "rating": 4.5,
     "features": ["natural"], "retailer": "Amazon"},

    {"name": "Organic Sugar 1kg", "brand": "Natureland", "price": 99, "rating": 4.3,
     "features": ["organic"], "retailer": "Amazon"},
])

bulk_insert("tea", [
    {"name": "Tata Tea Premium 1kg", "brand": "Tata", "price": 499, "rating": 4.5,
     "features": ["strong flavor"], "retailer": "Amazon"},

    {"name": "Red Label Tea 1kg", "brand": "Brooke Bond", "price": 459, "rating": 4.4,
     "features": ["rich aroma"], "retailer": "Flipkart"},

    {"name": "Green Tea 100 Bags", "brand": "Lipton", "price": 329, "rating": 4.6,
     "features": ["healthy"], "retailer": "Amazon"},

    {"name": "Masala Tea 1kg", "brand": "Wagh Bakri", "price": 520, "rating": 4.5,
     "features": ["masala blend"], "retailer": "Amazon"},

    {"name": "Organic Tea 250g", "brand": "24 Mantra", "price": 199, "rating": 4.3,
     "features": ["organic"], "retailer": "Flipkart"},

    {"name": "Darjeeling Tea 250g", "brand": "Twinings", "price": 599, "rating": 4.6,
     "features": ["premium"], "retailer": "Amazon"},

    {"name": "Classic Black Tea 250g", "brand": "Tetley", "price": 249, "rating": 4.4,
     "features": ["strong"], "retailer": "Amazon"},
])

bulk_insert("coffee", [
    {"name": "Nescafé Classic 200g", "brand": "Nescafé", "price": 349, "rating": 4.6,
     "features": ["instant coffee"], "retailer": "Amazon"},

    {"name": "Bru Instant Coffee 200g", "brand": "Bru", "price": 299, "rating": 4.5,
     "features": ["rich flavor"], "retailer": "Amazon"},

    {"name": "Filter Coffee 500g", "brand": "Cothas", "price": 299, "rating": 4.4,
     "features": ["south Indian blend"], "retailer": "Flipkart"},

    {"name": "Premium Instant Coffee 200g", "brand": "Continental", "price": 239, "rating": 4.3,
     "features": ["strong"], "retailer": "Amazon"},

    {"name": "Cold Brew Coffee 250g", "brand": "Blue Tokai", "price": 699, "rating": 4.7,
     "features": ["fresh roasted"], "retailer": "Amazon"},

    {"name": "Arabica Ground Coffee 250g", "brand": "Starbucks", "price": 749, "rating": 4.6,
     "features": ["arabica"], "retailer": "Amazon"},

    {"name": "Instant Coffee 200g", "brand": "Sunrise", "price": 249, "rating": 4.4,
     "features": ["instant blend"], "retailer": "Flipkart"},
])
bulk_insert("operating_system_book", [
    {"name": "Operating System Concepts", "brand": "Silberschatz", "price": 799, "rating": 4.7,
     "features": ["10th edition", "core OS fundamentals"], "retailer": "Amazon"},

    {"name": "Modern Operating Systems", "brand": "Andrew S. Tanenbaum", "price": 899, "rating": 4.8,
     "features": ["4th edition", "modern OS architecture"], "retailer": "Flipkart"},

    {"name": "Operating System Principles", "brand": "William Stallings", "price": 699, "rating": 4.5,
     "features": ["system structures", "process management"], "retailer": "Amazon"},

    {"name": "Operating Systems: A Practical Approach", "brand": "N. Chouksey", "price": 599, "rating": 4.3,
     "features": ["practical examples"], "retailer": "Amazon"},

    {"name": "Operating Systems: Internals and Design Principles", "brand": "Pearson", "price": 749, "rating": 4.4,
     "features": ["case studies"], "retailer": "Flipkart"},

    {"name": "Linux System Programming", "brand": "Robert Love", "price": 999, "rating": 4.6,
     "features": ["Linux-based OS"], "retailer": "Amazon"},

    {"name": "The Design of the UNIX Operating System", "brand": "Maurice Bach", "price": 849, "rating": 4.7,
     "features": ["UNIX architecture"], "retailer": "Amazon"},
])

bulk_insert("engineering_mathematics_book", [
    {"name": "Advanced Engineering Mathematics", "brand": "Erwin Kreyszig", "price": 999, "rating": 4.8,
     "features": ["global edition", "multidisciplinary"], "retailer": "Amazon"},

    {"name": "Higher Engineering Mathematics", "brand": "B.S. Grewal", "price": 699, "rating": 4.6,
     "features": ["classic reference"], "retailer": "Flipkart"},

    {"name": "Engineering Mathematics", "brand": "K. A. Stroud", "price": 899, "rating": 4.7,
     "features": ["comprehensive"], "retailer": "Amazon"},

    {"name": "Advanced Engineering Mathematics", "brand": "H. K. Dass", "price": 649, "rating": 4.5,
     "features": ["step-by-step solutions"], "retailer": "Amazon"},

    {"name": "GATE Engineering Mathematics", "brand": "Made Easy", "price": 549, "rating": 4.4,
     "features": ["GATE preparation"], "retailer": "Flipkart"},

    {"name": "Engineering Mathematics Vol-1", "brand": "B.V. Ramana", "price": 599, "rating": 4.3,
     "features": ["first-year syllabus"], "retailer": "Amazon"},

    {"name": "Advanced Engineering Mathematics", "brand": "Peter O’Neil", "price": 749, "rating": 4.5,
     "features": ["applied mathematics"], "retailer": "Amazon"},
])

bulk_insert("nvidia_geforce_rtx_gpu", [
    {"name": "NVIDIA GeForce RTX 3060 12GB", "brand": "NVIDIA", "price": 32999, "rating": 4.7,
     "features": ["12GB GDDR6", "ray tracing"], "retailer": "Amazon"},

    {"name": "NVIDIA GeForce RTX 3070 8GB", "brand": "NVIDIA", "price": 45999, "rating": 4.8,
     "features": ["8GB GDDR6", "DLSS"], "retailer": "Flipkart"},

    {"name": "NVIDIA GeForce RTX 3080 10GB", "brand": "NVIDIA", "price": 62999, "rating": 4.9,
     "features": ["10GB GDDR6X", "4K gaming"], "retailer": "Amazon"},

    {"name": "NVIDIA GeForce RTX 4060 8GB", "brand": "NVIDIA", "price": 28999, "rating": 4.6,
     "features": ["Ada Lovelace", "DLSS 3.0"], "retailer": "Amazon"},

    {"name": "NVIDIA GeForce RTX 4070 12GB", "brand": "NVIDIA", "price": 59999, "rating": 4.8,
     "features": ["12GB GDDR6X", "high efficiency"], "retailer": "Amazon"},

    {"name": "NVIDIA GeForce RTX 4090 24GB", "brand": "NVIDIA", "price": 159999, "rating": 4.9,
     "features": ["24GB GDDR6X", "ultimate performance"], "retailer": "Amazon"},

    {"name": "NVIDIA GeForce RTX 3050 8GB", "brand": "NVIDIA", "price": 22999, "rating": 4.5,
     "features": ["entry-level RTX", "8GB GDDR6"], "retailer": "Flipkart"},
])

bulk_insert("ram", [
    {"name": "Corsair Vengeance LPX 8GB DDR4", "brand": "Corsair", "price": 2499, "rating": 4.7,
     "features": ["3200MHz", "low profile"], "retailer": "Amazon"},

    {"name": "ADATA XPG 16GB DDR4", "brand": "ADATA", "price": 3499, "rating": 4.6,
     "features": ["3200MHz", "gaming RAM"], "retailer": "Flipkart"},

    {"name": "G.Skill Trident Z RGB 16GB DDR4", "brand": "G.Skill", "price": 6999, "rating": 4.8,
     "features": ["3600MHz", "RGB lighting"], "retailer": "Amazon"},

    {"name": "Kingston Fury Beast 8GB DDR4", "brand": "Kingston", "price": 2599, "rating": 4.5,
     "features": ["3200MHz"], "retailer": "Amazon"},

    {"name": "Crucial 16GB DDR4", "brand": "Crucial", "price": 3799, "rating": 4.7,
     "features": ["3200MHz", "high efficiency"], "retailer": "Flipkart"},

    {"name": "Samsung 8GB DDR4", "brand": "Samsung", "price": 2299, "rating": 4.6,
     "features": ["2666MHz"], "retailer": "Amazon"},

    {"name": "HyperX Predator 16GB DDR4", "brand": "HyperX", "price": 7499, "rating": 4.8,
     "features": ["4000MHz", "high performance"], "retailer": "Amazon"},
])

    

print("✔ Inserted laptops & smartwatches (7 each).")


if __name__ == "__main__":
    seed_custom_products()
