# Function to read products from a file and return a dictionary
def read_products(file_path):
    products = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                product_id = parts[0]
                product_name = parts[1]
                price = float(parts[2])
                products[product_id] = {'name': product_name, 'price': price}
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None
    return products

# Function to generate the bill and save it to a file
def generate_bill(purchases, products, bill_file):
    total_bill = 0
    bill_lines = ["BILL SUMMARY", "-----------------------------------"]
    
    for product_id, quantity in purchases.items():
        if product_id in products:
            product_name = products[product_id]['name']
            unit_price = products[product_id]['price']
            total_price = unit_price * quantity
            total_bill += total_price
            bill_lines.append(f"Product ID: {product_id}, Product Name: {product_name}, Quantity: {quantity}, Unit Price: {unit_price:.2f}, Total: {total_price:.2f}")
        else:
            bill_lines.append(f"Product ID: {product_id} not found.")
    
    bill_lines.append("-----------------------------------")
    bill_lines.append(f"Total Bill: {total_bill:.2f}")
    
    try:
        with open(bill_file, 'w') as file:
            file.write('\n'.join(bill_lines))
    except Exception as e:
        print(f"An error occurred while writing the bill: {e}")
    
    print('\n'.join(bill_lines))

def main():
    products_file = 'products.txt'
    bill_file = 'bill.txt'
    products = read_products(products_file)
    
    if products is None:
        return
    
    purchases = {}
    
    print("Enter the product details for billing. Type 'done' when you are finished.")
    
    while True:
        product_id = input("Enter product ID (or 'done' to finish): ").strip()
        if product_id.lower() == 'done':
            break
        if product_id not in products:
            print("Invalid product ID. Please try again.")
            continue
        try:
            quantity = int(input("Enter quantity: ").strip())
            if quantity <= 0:
                print("Quantity should be a positive integer. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number for quantity.")
            continue
        
        if product_id in purchases:
            purchases[product_id] += quantity
        else:
            purchases[product_id] = quantity
    
    if not purchases:
        print("No purchases made.")
    else:
        generate_bill(purchases, products, bill_file)
        print(f"The bill has been generated and saved to {bill_file}")

if __name__ == "__main__":
    main()