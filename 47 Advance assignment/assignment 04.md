### Advanced Billing System Assignment

#### Objective:
Create an advanced billing system using Python for a console application. The program should allow users to add products, apply discounts and taxes, generate bills, and handle multiple billing operations efficiently.

#### Assignment Questions:

**Question 1: Basic Billing System**

1. **Product Management:**
    - Add a Product
    - View All Products

2. **Billing Operations:**
    - Add Products to Bill
    - View Current Bill
    - Calculate Total with Discounts and Taxes
    - Generate Final Bill

### Features to Implement:
- **Function to Add a Product**: Create a function that allows the user to add new products with details like product ID, name, price, and stock quantity.
- **Function to View All Products**: Create a function that displays all available products.
- **Function to Add Products to Bill**: Create a function that allows the user to add products to the current bill.
- **Function to View Current Bill**: Create a function that displays the current bill with all added products.
- **Function to Calculate Total**: Create a function that calculates the total amount including discounts and taxes.
- **Function to Generate Final Bill**: Create a function that generates and displays the final bill, and reduces the stock quantity accordingly.

### Example Output:

```
Billing System
--------------
1. Add a Product
2. View All Products
3. Add Products to Bill
4. View Current Bill
5. Calculate Total
6. Generate Final Bill
7. Exit

Enter your choice: 1

Enter Product ID: P101
Enter Product Name: Apple
Enter Product Price: 50
Enter Product Quantity: 100
Product added successfully!

Billing System
--------------
1. Add a Product
2. View All Products
3. Add Products to Bill
4. View Current Bill
5. Calculate Total
6. Generate Final Bill
7. Exit

Enter your choice: 2

Available Products:
1. Product ID: P101, Name: Apple, Price: 50, Quantity: 100
```

**Question 2: Enhanced Billing Features**

1. **Discount Management:**
    - Apply Percentage Discount
    - Apply Fixed Discount

2. **Tax Management:**
    - Apply GST (Goods and Services Tax)
    - Apply Other Taxes (if applicable)

### Additional Features to Implement:
- **Function to Apply Discounts**: Create functions to apply both percentage and fixed discounts to the bill.
- **Function to Apply Taxes**: Create functions to apply GST and other applicable taxes to the bill.

### Example Output with Enhanced Features:

```
Billing System
--------------
1. Add a Product
2. View All Products
3. Add Products to Bill
4. View Current Bill
5. Apply Discount
6. Apply Tax
7. Calculate Total
8. Generate Final Bill
9. Exit

Enter your choice: 5

Enter Discount Type (percentage/fixed): percentage
Enter Discount Value: 10
Discount applied successfully!

Billing System
--------------
1. Add a Product
2. View All Products
3. Add Products to Bill
4. View Current Bill
5. Apply Discount
6. Apply Tax
7. Calculate Total
8. Generate Final Bill
9. Exit

Enter your choice: 6

Enter GST Percentage: 18
GST applied successfully!
```

**Question 3: Advanced Billing Features**

1. **Customer Management:**
    - Add Customer Details
    - View Customer Details

2. **Multiple Billing Sessions:**
    - Start New Bill
    - Save Current Bill
    - Load Saved Bill

3. **Data Persistence:**
    - Save and Load Product Data
    - Save and Load Customer Data
    - Save and Load Billing Data

### Features to Implement:
- **Function to Manage Customer Details**: Create functions to add and view customer details.
- **Function to Handle Multiple Billing Sessions**: Create functions to start a new bill, save the current bill, and load a saved bill.
- **Function for Data Persistence**: Create functions to save and load product, customer, and billing data.

### Example Output with Advanced Features:

```
Billing System
--------------
1. Add a Product
2. View All Products
3. Add Products to Bill
4. View Current Bill
5. Apply Discount
6. Apply Tax
7. Calculate Total
8. Generate Final Bill
9. Add Customer Details
10. View Customer Details
11. Start New Bill
12. Save Current Bill
13. Load Saved Bill
14. Exit

Enter your choice: 9

Enter Customer Name: John Doe
Enter Customer Phone: 1234567890
Enter Customer Email: john@example.com
Customer details added successfully!

Billing System
--------------
1. Add a Product
2. View All Products
3. Add Products to Bill
4. View Current Bill
5. Apply Discount
6. Apply Tax
7. Calculate Total
8. Generate Final Bill
9. Add Customer Details
10. View Customer Details
11. Start New Bill
12. Save Current Bill
13. Load Saved Bill
14. Exit

Enter your choice: 11

Starting new bill...
```

### Example Python Code for Basic Functionality:

```python
import json

def add_product(products):
    product_id = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    price = float(input("Enter Product Price: "))
    quantity = int(input("Enter Product Quantity: "))
    products[product_id] = {'name': name, 'price': price, 'quantity': quantity}
    print("Product added successfully!")

def view_products(products):
    print("Available Products:")
    for product_id, details in products.items():
        print(f"Product ID: {product_id}, Name: {details['name']}, Price: {details['price']}, Quantity: {details['quantity']}")

def add_to_bill(bill, products):
    product_id = input("Enter Product ID to Add: ")
    if product_id in products and products[product_id]['quantity'] > 0:
        quantity = int(input("Enter Quantity: "))
        if quantity <= products[product_id]['quantity']:
            if product_id in bill:
                bill[product_id]['quantity'] += quantity
            else:
                bill[product_id] = {'name': products[product_id]['name'], 'price': products[product_id]['price'], 'quantity': quantity}
            products[product_id]['quantity'] -= quantity
            print("Product added to bill!")
        else:
            print("Insufficient stock!")
    else:
        print("Product not available.")

def view_current_bill(bill):
    print("Current Bill:")
    for product_id, details in bill.items():
        print(f"Product ID: {product_id}, Name: {details['name']}, Price: {details['price']}, Quantity: {details['quantity']}, Subtotal: {details['price']*details['quantity']}")

def calculate_total(bill, discount=0, gst=0):
    total = sum(details['price'] * details['quantity'] for details in bill.values())
    if discount > 0:
        total -= total * (discount / 100)
    if gst > 0:
        total += total * (gst / 100)
    return total

def generate_final_bill(bill, discount=0, gst=0):
    total = calculate_total(bill, discount, gst)
    view_current_bill(bill)
    print(f"Total Amount (after discount and tax): {total}")
    print("Final Bill generated successfully!")

def save_data(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)
    print(f"Data saved to {filename}")

def load_data(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def main():
    products = load_data('products.json')
    customers = load_data('customers.json')
    bill = {}
    
    while True:
        print("\nBilling System")
        print("--------------")
        print("1. Add a Product")
        print("2. View All Products")
        print("3. Add Products to Bill")
        print("4. View Current Bill")
        print("5. Apply Discount")
        print("6. Apply Tax")
        print("7. Calculate Total")
        print("8. Generate Final Bill")
        print("9. Add Customer Details")
        print("10. View Customer Details")
        print("11. Start New Bill")
        print("12. Save Current Bill")
        print("13. Load Saved Bill")
        print("14. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_product(products)
        elif choice == '2':
            view_products(products)
        elif choice == '3':
            add_to_bill(bill, products)
        elif choice == '4':
            view_current_bill(bill)
        elif choice == '5':
            discount = float(input("Enter Discount Percentage: "))
        elif choice == '6':
            gst = float(input("Enter GST Percentage: "))
        elif choice == '7':
            total = calculate_total(bill, discount, gst)
            print(f"Total Amount: {total}")
        elif choice == '8':
            generate_final_bill(bill, discount, gst)
        elif choice == '9':
            customer_id = input("Enter Customer ID: ")
            name = input("Enter Customer Name: ")
            phone = input("Enter Customer Phone: ")
            email = input("Enter Customer Email: ")
            customers[customer_id] = {'name': name, 'phone': phone, 'email': email}
            print("Customer details added successfully!")
        elif choice == '10':
            for customer_id, details in customers.items():
                print(f"Customer ID: {customer_id}, Name: {details['name']}, Phone: {details['phone']}, Email: {details['email']}")
        elif choice == '11':
            bill = {}
            print("Starting new bill...")
        elif choice == '12':
            save_data(bill, 'current_bill.json')
        elif choice == '13':
            bill = load_data('current_bill.json')
            print("Bill loaded successfully!")
        elif choice == '14':
            save_data(products, 'products.json')
            save_data(customers, 'customers.json')
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

This assignment helps students understand how to create an advanced billing system using Python functions. It covers product and customer management, billing operations, discount and tax application, multiple billing sessions, and data persistence.