# 🛒 Smart Grocery Store Management System

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Interface](https://img.shields.io/badge/Interface-CLI-black?logo=gnubash&logoColor=white)
![Dependencies](https://img.shields.io/badge/Dependencies-None-brightgreen)
![Status](https://img.shields.io/badge/Status-Active-success)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)
![License](https://img.shields.io/badge/License-MIT-blue)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-ff69b4)

A simple, beginner-friendly **command-line inventory and sales system** for a grocery store, written in pure Python. Manage products, track stock, process customer purchases, and generate store reports, all from an interactive menu with no external libraries.

---

## 📑 Table of Contents

- [Features](#-features)
- [Demo](#-demo)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Data Structures](#-data-structures)
- [Project Structure](#-project-structure)
- [Test Cases](#-test-cases)
- [Automated Smoke Test](#-automated-smoke-test)
- [Known Limitations](#-known-limitations)
- [Future Improvements](#-future-improvements)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

| # | Feature | Description |
|---|---------|-------------|
| 1 | **Add Product** | Add a new item with ID, name, category, price, and stock |
| 2 | **View Products** | List every product in the inventory |
| 3 | **Search Product** | Find a product by exact name (case-insensitive) or by ID |
| 4 | **Update Stock** | Add to the current stock or set a new quantity |
| 5 | **Process Sale** | Sell a product, deduct stock, and record the sale |
| 6 | **View Sales** | Show every recorded sale |
| 7 | **Store Report** | Totals, revenue, low-stock alerts, highest and lowest priced products |
| 8 | **Exit** | Close the program |

Plus built-in **input validation** for IDs, prices, quantities, and stock levels.

---

## 🎬 Demo

```text
====================================
     SMART GROCERY STORE SYSTEM
====================================
1. Add New Product
2. View All Products
3. Search Product
4. Update Product Stock
5. Process Customer Sale
6. View Sales Records
7. Generate Store Report
8. Exit

Enter your choice: 5

--- Customer Sale ---
Enter Product ID: 103
Enter Purchase Quantity: 3

--- Purchase Summary ---
Product: Rice
Quantity: 3
Price: Rs. 300
Total Amount: Rs. 900
Remaining Stock: 12
Sale completed successfully!
```

---

## 🚀 Getting Started

### Prerequisites

- [Python 3.8 or higher](https://www.python.org/downloads/)

Check your version:

```bash
python --version
```

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/smart-grocery-store.git

# 2. Move into the project folder
cd smart-grocery-store

# 3. Run the program
python grocery_store.py
```

> No `pip install` needed. The project uses only Python's standard features.

---

## 📖 Usage

Run the script and pick an option from the menu by typing its number (1 to 8).

### Pre-loaded sample products

| ID | Name | Category | Price (Rs.) | Stock |
|----|------|----------|-------------|-------|
| 101 | Milk | Dairy | 250 | 20 |
| 102 | Bread | Bakery | 150 | 10 |
| 103 | Rice | Food | 300 | 15 |

> ⚠️ Data is stored **in memory only**. Everything resets when you exit the program.

---

## 🧱 Data Structures

**Product**

```python
{"id": 101, "name": "Milk", "category": "Dairy", "price": 250, "stock": 20}
```

**Sale record**

```python
{"product_id": 101, "product_name": "Milk", "quantity_sold": 2, "total_amount": 500}
```

Both are kept in plain Python lists: `products` and `sales`.

---

## 📂 Project Structure

```text
smart-grocery-store/
├── grocery_store.py   # Main application
└── README.md          # Project documentation
```

### Functions overview

| Function | Purpose |
|----------|---------|
| `find_product(product_id)` | Returns the product with the given ID, or `None` |
| `add_product()` | Validates input and adds a new product |
| `view_products()` | Prints all products |
| `search_product()` | Searches by name or ID |
| `update_stock()` | Increases or resets stock |
| `process_sale()` | Handles a purchase and logs the sale |
| `view_sales()` | Prints all sales records |
| `store_report()` | Prints summary statistics |

---

## 🧪 Test Cases

Run `python grocery_store.py` and follow the steps below. All expected results assume a **fresh start** with the three sample products (state carries over between tests within one run).

### 1️⃣ Add Product

| ID | Test Scenario | Input | Expected Output |
|----|---------------|-------|-----------------|
| TC-A1 | Valid product | ID `104`, Name `Eggs`, Category `Poultry`, Price `200`, Stock `30` | `Product added successfully!` |
| TC-A2 | Non-numeric ID | ID `abc` | `Invalid ID! Enter numbers only.` |
| TC-A3 | Negative ID | ID `-5` | `Invalid ID! Enter numbers only.` |
| TC-A4 | Duplicate ID | ID `101` | `This Product ID already exists!` |
| TC-A5 | Non-numeric price | ID `105`, Price `ten` | `Price and stock must be numbers!` |
| TC-A6 | Non-numeric stock | ID `105`, Stock `many` | `Price and stock must be numbers!` |
| TC-A7 | Empty name | ID `105`, Name (blank) | `Please enter valid product information!` |
| TC-A8 | Empty category | ID `105`, Category (blank) | `Please enter valid product information!` |
| TC-A9 | Zero price | ID `105`, Price `0` | `Please enter valid product information!` |
| TC-A10 | Zero stock (allowed) | ID `105`, Price `50`, Stock `0` | `Product added successfully!` |

### 2️⃣ View Products

| ID | Test Scenario | Expected Output |
|----|---------------|-----------------|
| TC-V1 | Default inventory | Shows Milk, Bread, Rice with all details |
| TC-V2 | After adding a product | The new product appears in the list |

### 3️⃣ Search Product

| ID | Test Scenario | Input | Expected Output |
|----|---------------|-------|-----------------|
| TC-S1 | Search by ID | `101` | `Product Found!` with Milk details |
| TC-S2 | Search by name | `Bread` | `Product Found!` with Bread details |
| TC-S3 | Case-insensitive name | `rIcE` | `Product Found!` with Rice details |
| TC-S4 | Name with spaces around | `  Milk  ` | `Product Found!` (input is trimmed) |
| TC-S5 | Unknown product | `Butter` | `Product not found!` |
| TC-S6 | Unknown ID | `999` | `Product not found!` |
| TC-S7 | Partial name | `Mil` | `Product not found!` (exact match only) |

### 4️⃣ Update Stock

| ID | Test Scenario | Input | Expected Output |
|----|---------------|-------|-----------------|
| TC-U1 | Add stock | ID `101`, choice `1`, qty `10` | `Stock added successfully!`, Updated Stock: `30` |
| TC-U2 | Set new stock | ID `102`, choice `2`, qty `50` | `Stock updated successfully!`, Updated Stock: `50` |
| TC-U3 | Set stock to zero | ID `102`, choice `2`, qty `0` | `Stock updated successfully!`, Updated Stock: `0` |
| TC-U4 | Add zero quantity | ID `101`, choice `1`, qty `0` | `Enter a valid quantity!` |
| TC-U5 | Add negative quantity | ID `101`, choice `1`, qty `-3` | `Enter a valid quantity!` |
| TC-U6 | Non-numeric quantity | ID `101`, choice `2`, qty `abc` | `Enter a valid quantity!` |
| TC-U7 | Invalid menu choice | ID `101`, choice `9` | `Invalid choice!` |
| TC-U8 | Non-numeric ID | ID `xyz` | `Invalid Product ID!` |
| TC-U9 | Unknown ID | ID `999` | `Product not found!` |

### 5️⃣ Process Sale

| ID | Test Scenario | Input | Expected Output |
|----|---------------|-------|-----------------|
| TC-P1 | Valid sale | ID `103`, qty `3` | Total: Rs. `900`, Remaining Stock: `12`, `Sale completed successfully!` |
| TC-P2 | Sell entire stock | ID `102`, qty `10` | Remaining Stock: `0`, sale completes |
| TC-P3 | Sell more than stock | ID `101`, qty `21` | `Sorry! Not enough stock available.` |
| TC-P4 | Sell zero | ID `101`, qty `0` | `Enter a valid purchase quantity!` |
| TC-P5 | Negative quantity | ID `101`, qty `-2` | `Enter a valid purchase quantity!` |
| TC-P6 | Non-numeric quantity | ID `101`, qty `two` | `Enter a valid purchase quantity!` |
| TC-P7 | Non-numeric ID | ID `abc` | `Invalid Product ID!` |
| TC-P8 | Unknown ID | ID `999` | `Product not found!` |
| TC-P9 | Out-of-stock product | After TC-P2, sell ID `102`, qty `1` | `Sorry! Not enough stock available.` |

### 6️⃣ View Sales

| ID | Test Scenario | Expected Output |
|----|---------------|-----------------|
| TC-R1 | No sales yet | `No sales records available.` |
| TC-R2 | After TC-P1 | Shows Rice, quantity `3`, total Rs. `900` |
| TC-R3 | Failed sale (TC-P3) | No new record is added |

### 7️⃣ Store Report

| ID | Test Scenario | Expected Output |
|----|---------------|-----------------|
| TC-T1 | Fresh start | Products: `3`, Stock: `45`, Transactions: `0`, Revenue: Rs. `0` |
| TC-T2 | Low-stock check (fresh) | `No products have low stock.` |
| TC-T3 | Price comparison (fresh) | Highest: Rice (Rs. 300), Lowest: Bread (Rs. 150) |
| TC-T4 | After selling 3 Rice | Transactions: `1`, Revenue: Rs. `900`, Stock: `42` |
| TC-T5 | After selling 6 Bread (stock 4) | Low stock list shows `Bread - 4 units` |
| TC-T6 | Stock exactly 5 | Product is **not** listed (rule is `stock < 5`) |

### 8️⃣ Main Menu

| ID | Test Scenario | Input | Expected Output |
|----|---------------|-------|-----------------|
| TC-M1 | Valid choice | `2` | Product list is displayed |
| TC-M2 | Out-of-range choice | `9` | `Invalid choice! Please select 1 to 8.` |
| TC-M3 | Non-numeric choice | `abc` | `Invalid choice! Please select 1 to 8.` |
| TC-M4 | Empty input | (press Enter) | `Invalid choice! Please select 1 to 8.` |
| TC-M5 | Exit | `8` | `Thank you for using Grocery Store System!` and the program ends |

---

## 🤖 Automated Smoke Test

You can feed inputs to the program without typing, by piping them in.

**Linux / macOS (bash):**

```bash
printf "5\n103\n3\n7\n8\n" | python grocery_store.py
```

This sells 3 units of Rice, shows the store report, then exits. In the output, check for:

```text
Total Amount: Rs. 900
Remaining Stock: 12
Total Revenue: Rs. 900
```

**Windows (PowerShell):**

```powershell
"5`n103`n3`n7`n8" | python grocery_store.py
```

> 💡 **Tip for unit testing:** the menu loop runs at import time, so you can't `import` the functions into `pytest` as is. Wrap the main loop in `if __name__ == "__main__":` to make the functions testable. Example:
>
> ```python
> # test_grocery.py
> from grocery_store import find_product
>
> def test_find_existing_product():
>     assert find_product(101)["name"] == "Milk"
>
> def test_find_missing_product():
>     assert find_product(999) is None
> ```
>
> Run with `pytest -v`.

---

## ⚠️ Known Limitations

- Data is **not saved** to disk, so it is lost on exit.
- Search matches **exact** names only (no partial matching).
- Prices and stock must be **whole numbers** (no decimals).
- No duplicate-name check (two products can share a name if IDs differ).
- No receipt for multi-item purchases (one product per sale).

---

## 🔮 Future Improvements

- [ ] Save and load data using JSON or CSV files
- [ ] Support decimal prices
- [ ] Partial and category-based search
- [ ] Multi-item shopping cart and receipts
- [ ] Delete and edit product details
- [ ] Sales history with dates and times
- [ ] Unit tests with `pytest`
- [ ] GUI or web interface

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m "Add amazing feature"`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

⭐ If you found this project useful, consider giving it a star!