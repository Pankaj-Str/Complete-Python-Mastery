# Billing System using File Handling

## Assignment: Create a Billing System using File Handling

Welcome to this assignment on creating a billing system using file handling in Python, brought to you by codeswithpankaj.com. In this assignment, we will build a simple billing system that reads product information from a file, allows users to select products, calculates the total bill, and writes the transaction details to another file.

### Table of Contents

1. Introduction
2. System Requirements
3. Setting Up the Project
4. Reading Product Information
5. Displaying Products
6. Handling User Selection
7. Calculating the Total Bill
8. Writing Transaction Details
9. Running the Billing System
10. Conclusion

***

### 1. Introduction

In this assignment, we will create a billing system that performs the following tasks:

* Reads product information from a file
* Displays available products to the user
* Allows the user to select products and quantities
* Calculates the total bill
* Writes the transaction details to a file

### 2. System Requirements

To complete this assignment, you will need:

* Python 3.x installed on your system
* A text editor or IDE for writing Python code

### 3. Setting Up the Project

Create a project directory for your billing system and set up the following files:

* `products.txt`: A file containing product information
* `billing_system.py`: The main Python script for the billing system
* `transactions.txt`: A file to store transaction details

#### Example `products.txt`

```plaintext
1,Apple,0.50
2,Banana,0.30
3,Orange,0.40
4,Milk,1.20
5,Bread,1.00
```

Each line in the `products.txt` file represents a product with the following format: `ProductID,ProductName,Price`

***

### 4. Reading Product Information

We will start by reading the product information from the `products.txt` file and storing it in a list of dictionaries.

#### Code Example

```python
def read_products(filename):
    products = []
    with open(filename, 'r') as file:
        for line in file:
            product_id, name, price = line.strip().split(',')
            products.append({
                'id': product_id,
                'name': name,
                'price': float(price)
            })
    return products

# Test reading products
products = read_products('products.txt')
for product in products:
    print(product)
```

***

### 5. Displaying Products

Next, we will create a function to display the available products to the user.

#### Code Example

```python
def display_products(products):
    print("Available Products:")
    print("{:<10} {:<15} {:<10}".format('ProductID', 'ProductName', 'Price'))
    for product in products:
        print("{:<10} {:<15} ${:<10.2f}".format(product['id'], product['name'], product['price']))

# Test displaying products
display_products(products)
```

***

### 6. Handling User Selection

We will create a function to handle user selection of products and quantities. This function will return a list of selected products with their quantities.

#### Code Example

```python
def select_products(products):
    selected_products = []
    while True:
        product_id = input("Enter the ProductID to add to the cart (or 'done' to finish): ")
        if product_id.lower() == 'done':
            break
        quantity = int(input("Enter the quantity: "))
        for product in products:
            if product['id'] == product_id:
                selected_products.append({
                    'id': product['id'],
                    'name': product['name'],
                    'price': product['price'],
                    'quantity': quantity
                })
                break
        else:
            print("Invalid ProductID")
    return selected_products

# Test selecting products
selected_products = select_products(products)
for product in selected_products:
    print(product)
```

***

### 7. Calculating the Total Bill

We will create a function to calculate the total bill based on the selected products and their quantities.

#### Code Example

```python
def calculate_total(selected_products):
    total = 0
    for product in selected_products:
        total += product['price'] * product['quantity']
    return total

# Test calculating total bill
total = calculate_total(selected_products)
print("Total Bill: ${:.2f}".format(total))
```

***

### 8. Writing Transaction Details

We will create a function to write the transaction details to the `transactions.txt` file.

#### Code Example

```python
def write_transaction(filename, selected_products, total):
    with open(filename, 'a') as file:
        file.write("Transaction:\n")
        for product in selected_products:
            file.write("{:<10} {:<15} ${:<10.2f} x {}\n".format(product['id'], product['name'], product['price'], product['quantity']))
        file.write("Total: ${:.2f}\n".format(total))
        file.write("\n")

# Test writing transaction
write_transaction('transactions.txt', selected_products, total)
```

***

### 9. Running the Billing System

Finally, we will combine all the functions and run the billing system.

#### Code Example

```python
def main():
    products = read_products('products.txt')
    display_products(products)
    selected_products = select_products(products)
    total = calculate_total(selected_products)
    print("Total Bill: ${:.2f}".format(total))
    write_transaction('transactions.txt', selected_products, total)
    print("Transaction details have been saved to 'transactions.txt'.")

if __name__ == "__main__":
    main()
```

***

### 10. Conclusion

This concludes our assignment on creating a billing system using file handling in Python. We hope you found this assignment helpful and informative. For more tutorials and resources, visit codeswithpankaj.com. Happy coding!
