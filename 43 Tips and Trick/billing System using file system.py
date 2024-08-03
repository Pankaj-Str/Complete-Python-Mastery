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
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
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
            bill_lines.append(f"Product ID: {product_id}, Product Name: {product_name}, Quantity: {quantity}, Unit Price: {unit_price}, Total: {total_price}")
        else:
            bill_lines.append(f"Product ID: {product_id} not found.")
    
    bill_lines.append("-----------------------------------")
    bill_lines.append(f"Total Bill: {total_bill}")
    
    with open(bill_file, 'w') as file:
        file.write('\n'.join(bill_lines))
    
    print('\n'.join(bill_lines))

def main():
    products_file = 'products.txt'
    bill_file = 'bill.txt'
    products = read_products(products_file)
    
    if not products:
        return
    
    purchases = {}
    
    while True:
        try:
            product_id = input("Enter product ID (or 'done' to finish): ")
            if product_id.lower() == 'done':
                break
            quantity = int(input("Enter quantity: "))
            if product_id in purchases:
                purchases[product_id] += quantity
            else:
                purchases[product_id] = quantity
        except ValueError:
            print("Invalid input. Please enter a valid number for quantity.")
    
    generate_bill(purchases, products, bill_file)

if __name__ == "__main__":
    main()