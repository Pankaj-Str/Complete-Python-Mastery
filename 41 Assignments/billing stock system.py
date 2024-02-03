products = []

while True:
    sku = input("Enter SKU: ")
    name = input("Enter Product Name: ")
    quantity = int(input("Enter Quantity: "))
    price = int(input("Enter Price: "))

    product = {"SKU": sku, "Name": name, "Quantity": quantity, "Price": price}
    products.append(product)

    add_more = input("Add more products? (Y/N): ")
    if add_more.upper() != 'Y':
        break

print("\n------ Search Item ------")
search_sku = input("Enter SKU to search: ")

found_product = next((p for p in products if p["SKU"] == search_sku), None)

if found_product:
    total_cost = found_product["Quantity"] * found_product["Price"]
    print(f"Total Cost: {total_cost}/-\nProduct Name: {found_product['Name']}\nQuantity: {found_product['Quantity']}\nPrice: {found_product['Price']}/-")
else:
    print("Product not found.")
    
    
