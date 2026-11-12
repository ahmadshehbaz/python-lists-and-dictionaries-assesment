# 1. Store products in a list of dictionaries
products = [
    {
        "id": 101,
        "name": "Milk",
        "category": "Dairy",
        "price": 250,
        "stock": 20
    },
    {
        "id": 102,
        "name": "Bread",
        "category": "Bakery",
        "price": 150,
        "stock": 10
    },
    {
        "id": 103,
        "name": "Rice",
        "category": "Food",
        "price": 300,
        "stock": 15
    }
]
# 2. Store sales records
sales = []
# Function to find a product using its ID
def find_product(product_id):
    for product in products:
        if product["id"] == product_id:
            return product
    return None
# Function to add a new product
def add_product():
    print("\n--- Add New Product ---")
    product_id = input("Enter Product ID: ")
    if not product_id.isdigit():
        print("Invalid ID! Enter numbers only.")
        return
    product_id = int(product_id)
    if find_product(product_id) is not None:
        print("This Product ID already exists!")
        return
    name = input("Enter Product Name: ").strip()
    category = input("Enter Category: ").strip()
    price = input("Enter Price: ")
    stock = input("Enter Stock Quantity: ")
    if not price.isdigit() or not stock.isdigit():
        print("Price and stock must be numbers!")
        return
    price = int(price)
    stock = int(stock)
    if name == "" or category == "" or price <= 0:
        print("Please enter valid product information!")
        return
    new_product = {
        "id": product_id,
        "name": name,
        "category": category,
        "price": price,
        "stock": stock
    }
    products.append(new_product)
    print("Product added successfully!")
# Function to display all products
def view_products():
    print("\n--- All Products ---")
    if len(products) == 0:
        print("No products available.")
        return
    for product in products:
        print("-------------------------")
        print("ID:", product["id"])
        print("Name:", product["name"])
        print("Category:", product["category"])
        print("Price: Rs.", product["price"])
        print("Stock:", product["stock"])
# Function to search for a product
def search_product():
    print("\n--- Search Product ---")
    search = input("Enter Product Name or ID: ").strip()
    found = False
    for product in products:
        if (search.lower() == product["name"].lower()
                or search == str(product["id"])):
            print("\nProduct Found!")
            print("ID:", product["id"])
            print("Name:", product["name"])
            print("Category:", product["category"])
            print("Price: Rs.", product["price"])
            print("Stock:", product["stock"])
            found = True
    if found == False:
        print("Product not found!")
# Function to update product stock
def update_stock():
    print("\n--- Update Stock ---")
    product_id = input("Enter Product ID: ")
    if not product_id.isdigit():
        print("Invalid Product ID!")
        return
    product_id = int(product_id)
    product = find_product(product_id)
    if product is None:
        print("Product not found!")
        return
    print("Current Stock:", product["stock"])
    print("1. Add More Stock")
    print("2. Set New Stock Quantity")
    choice = input("Enter your choice: ")
    if choice == "1":
        quantity = input("Enter quantity to add: ")
        if quantity.isdigit() and int(quantity) > 0:
            product["stock"] += int(quantity)
            print("Stock added successfully!")
        else:
            print("Enter a valid quantity!")
    elif choice == "2":
        quantity = input("Enter new stock quantity: ")
        if quantity.isdigit():
            product["stock"] = int(quantity)
            print("Stock updated successfully!")
        else:
            print("Enter a valid quantity!")
    else:
        print("Invalid choice!")
    print("Updated Stock:", product["stock"])
# Function to process a customer sale
def process_sale():
    print("\n--- Customer Sale ---")
    product_id = input("Enter Product ID: ")
    if not product_id.isdigit():
        print("Invalid Product ID!")
        return
    product_id = int(product_id)
    product = find_product(product_id)
    if product is None:
        print("Product not found!")
        return
    quantity = input("Enter Purchase Quantity: ")
    if not quantity.isdigit() or int(quantity) <= 0:
        print("Enter a valid purchase quantity!")
        return
    quantity = int(quantity)
    if quantity > product["stock"]:
        print("Sorry! Not enough stock available.")
        return
    total_price = product["price"] * quantity
    # Deduct sold quantity from available stock
    product["stock"] -= quantity
    # Save the sale record
    sale_record = {
        "product_id": product["id"],
        "product_name": product["name"],
        "quantity_sold": quantity,
        "total_amount": total_price
    }
    sales.append(sale_record)
    print("\n--- Purchase Summary ---")
    print("Product:", product["name"])
    print("Quantity:", quantity)
    print("Price: Rs.", product["price"])
    print("Total Amount: Rs.", total_price)
    print("Remaining Stock:", product["stock"])
    print("Sale completed successfully!")
# Function to view sales records
def view_sales():
    print("\n--- Sales Records ---")
    if len(sales) == 0:
        print("No sales records available.")
        return
    for sale in sales:
        print("-------------------------")
        print("Product ID:", sale["product_id"])
        print("Product Name:", sale["product_name"])
        print("Quantity Sold:", sale["quantity_sold"])
        print("Total Amount: Rs.", sale["total_amount"])
# Function to generate store report
def store_report():
    print("\n--- STORE REPORT ---")
    total_products = len(products)
    total_stock = 0
    total_revenue = 0
    for product in products:
        total_stock += product["stock"]
    for sale in sales:
        total_revenue += sale["total_amount"]
    total_transactions = len(sales)
    print("Total Products:", total_products)
    print("Total Available Stock:", total_stock)
    print("Total Sales Transactions:", total_transactions)
    print("Total Revenue: Rs.", total_revenue)
    # Find products with stock below 5
    print("\nProducts with Stock Below 5:")
    found = False
    for product in products:
        if product["stock"] < 5:
            print(product["name"], "-", product["stock"], "units")
            found = True
    if found == False:
        print("No products have low stock.")
    # Find highest and lowest price products
    if len(products) > 0:
        highest_price = products[0]
        lowest_price = products[0]
        for product in products:
            if product["price"] > highest_price["price"]:
                highest_price = product
            if product["price"] < lowest_price["price"]:
                lowest_price = product
        print("\nHighest Price Product:")
        print(highest_price["name"], "- Rs.", highest_price["price"])
        print("\nLowest Price Product:")
        print(lowest_price["name"], "- Rs.", lowest_price["price"])
    else:
        print("No products available for price comparison.")
# MAIN PROGRAM
while True:
    print("\n====================================")
    print("     SMART GROCERY STORE SYSTEM")
    print("====================================")
    print("1. Add New Product")
    print("2. View All Products")
    print("3. Search Product")
    print("4. Update Product Stock")
    print("5. Process Customer Sale")
    print("6. View Sales Records")
    print("7. Generate Store Report")
    print("8. Exit")
    choice = input("\nEnter your choice: ")
    if choice == "1":
        add_product()
    elif choice == "2":
        view_products()
    elif choice == "3":
        search_product()
    elif choice == "4":
        update_stock()
    elif choice == "5":
        process_sale()
    elif choice == "6":
        view_sales()
    elif choice == "7":
        store_report()
    elif choice == "8":
        print("Thank you for using Grocery Store System!")
        break
    else:
        print("Invalid choice! Please select 1 to 8.")
