def input_products():
    products = {"ids": [], "names": [], "quantities": [], "prices": [], "subtotals": []}
    while True:
        pid = int(input("Enter a product ID: "))
        if pid in products["ids"]:
            print("Product ID already exists. Please enter a different ID.")
            continue
        products["ids"].append(pid)
        products["names"].append(input("Enter a product name: "))
        products["quantities"].append(int(input("Enter the quantity: ")))
        products["prices"].append(int(input("Enter the unit price (₹): ")))
        if input("Add more items? [Y/N]: ").lower() == "n":
            break
        print("-----------------------------------")
    return products

def print_products(products):
    print("----------------PRODUCT LIST-----------------")
    for i, pid in enumerate(products["ids"]):
        print(f"Product ID: {pid}, Product Name: {products['names'][i]}, Quantity: {products['quantities'][i]}, Unit Price: ₹{products['prices'][i]}/-")
        print("-----------------------------------------")

def remove_product(products):
    if input("Remove a product? [Y/N]: ").lower() == "y":
        pid = int(input("Enter Product ID to remove: "))
        if pid in products["ids"]:
            idx = products["ids"].index(pid)
            for key in products:
                del products[key][idx]
            print("Product removed successfully")
            print("-----------------------------------")
            print_products(products)
        else:
            print("Product ID not found")
    else:
        print("No product removed")

def calculate_totals(products):
    products["subtotals"] = [q * p for q, p in zip(products["quantities"], products["prices"])]
    return sum(products["subtotals"])

def calculate_gst(total):
    if input("Add GST? [Y/N]: ").lower() == "y":
        gst_rate = int(input("Enter GST Rate: "))
        gst_amount = total * gst_rate / 100
        return total + gst_amount, gst_rate, gst_amount
    return total, 0, 0

def apply_discount(total):
    discounts = {
        "1": "Percentage Discount on Total Bill",
        "2": "Fixed Amount Discount on Total Bill",
        "3": "Discount on Specific Product"
    }
    for key, value in discounts.items():
        print(f"{key}: {value}")

    choice = input("Enter Choice: ")
    if choice == "1":
        rate = float(input("Enter Discount Rate (%): "))
        amount = total * rate / 100
        return total - amount, rate, amount
    elif choice == "2":
        amount = int(input("Enter Discount Amount (₹): "))
        return total - amount, 0, amount
    elif choice == "3":
        pid = int(input("Enter Product ID for discount: "))
        if pid in products["ids"]:
            idx = products["ids"].index(pid)
            rate = int(input(f"Enter Discount Rate on Product {products['names'][idx]} (%): "))
            amount = (rate / 100) * products["subtotals"][idx]
            total -= products["subtotals"][idx]
            total += products["subtotals"][idx] - amount
            return total, rate, amount
    print("Invalid Input")
    return total, 0, 0

def print_invoice(products, total, gst_rate, gst_amount, discount_rate, discount_amount):
    print("-----------------------------------")
    print("E-commerce Billing System Invoice")
    print("-----------------------------------")
    for i, pid in enumerate(products["ids"]):
        print(f"Product ID: {pid}")
        print(f"Product Name: {products['names'][i]}")
        print(f"Quantity: {products['quantities'][i]}")
        print(f"Unit Price: ₹{products['prices'][i]}/-")
        print(f"Subtotal: ₹{products['subtotals'][i]}/-")
        print("-----------------------------------")
    print(f"Total before discount: ₹{total}/-")
    print(f"GST @ {gst_rate}%: ₹{gst_amount}/-")
    if discount_rate:
        print(f"Discount @ {discount_rate}%: ₹{discount_amount}/-")
    else:
        print(f"Discount: ₹{discount_amount}/-")
    print(f"Final Total: ₹{total}/-")
    print("----------------------------------")
    print("Thank you for shopping with us!")
    print("-----------------------------------")

products = input_products()
print_products(products)
remove_product(products)
total = calculate_totals(products)
total_with_gst, gst_rate, gst_amount = calculate_gst(total)
if input("Add a discount? [Y/N]: ").lower() == "y":
    total_with_gst, discount_rate, discount_amount = apply_discount(total_with_gst)
else:
    discount_rate, discount_amount = 0, 0
print_invoice(products, total_with_gst, gst_rate, gst_amount, discount_rate, discount_amount)