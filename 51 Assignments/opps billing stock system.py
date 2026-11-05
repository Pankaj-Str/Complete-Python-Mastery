class Product:
    def __init__(self, sku, name, quantity, price):
        self.sku = sku
        self.name = name
        self.quantity = quantity
        self.price = price

def main():
    products = []

    while True:
        sku = input("Enter SKU: ")
        name = input("Enter Product Name: ")
        quantity = int(input("Enter Quantity: "))
        price = int(input("Enter Price: "))

        product = Product(sku, name, quantity, price)
        products.append(product)

        add_more = input("Add more products? (Y/N): ")
        if add_more.upper() != 'Y':
            break

    print("\n------ Search Item ------")
    search_sku = input("Enter SKU to search: ")

    found_product = next((p for p in products if p.sku == search_sku), None)

    if found_product:
        total_cost = found_product.quantity * found_product.price
        print(f"Total Cost: {total_cost}/-\nProduct Name: {found_product.name}\nQuantity: {found_product.quantity}\nPrice: {found_product.price}/-")
    else:
        print("Product not found.")

if __name__ == "__main__":
    main()