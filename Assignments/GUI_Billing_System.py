import tkinter as tk
from tkinter import ttk

class BillingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Billing System")

        # Menu Card
        self.menu = {
            "Item 1": 10.00,
            "Item 2": 15.00,
            "Item 3": 8.50,
            # Add more items as needed
        }

        # Variables
        self.selected_items = {}
        self.total_amount = tk.DoubleVar()

        # GUI Components
        self.create_menu_card()
        self.create_billing_section()

    def create_menu_card(self):
        frame_menu = ttk.LabelFrame(self.root, text="Menu Card")
        frame_menu.grid(row=0, column=0, padx=10, pady=10)

        for i, (item, price) in enumerate(self.menu.items(), start=1):
            ttk.Label(frame_menu, text=f"{item}: ${price:.2f}").grid(row=i, column=0, sticky="w")

            quantity_var = tk.IntVar()
            ttk.Spinbox(frame_menu, from_=0, to=10, textvariable=quantity_var).grid(row=i, column=1, padx=5)

            add_button = ttk.Button(frame_menu, text="Add", command=lambda item=item, price=price, quantity=quantity_var: self.add_to_cart(item, price, quantity))
            add_button.grid(row=i, column=2, padx=5)

    def create_billing_section(self):
        frame_billing = ttk.LabelFrame(self.root, text="Billing")
        frame_billing.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(frame_billing, text="Selected Items:").grid(row=0, column=0, sticky="w", pady=5)
        self.selected_items_label = ttk.Label(frame_billing, text="")
        self.selected_items_label.grid(row=1, column=0, sticky="w")

        ttk.Label(frame_billing, text="Total Amount:").grid(row=2, column=0, sticky="w", pady=5)
        ttk.Label(frame_billing, textvariable=self.total_amount).grid(row=2, column=1, sticky="w")

        ttk.Button(frame_billing, text="Generate Bill", command=self.generate_bill).grid(row=3, column=0, columnspan=2, pady=10)

    def add_to_cart(self, item, price, quantity_var):
        quantity = quantity_var.get()
        if quantity > 0:
            if item in self.selected_items:
                self.selected_items[item]["quantity"] += quantity
            else:
                self.selected_items[item] = {"price": price, "quantity": quantity}

            self.update_selected_items_label()

    def update_selected_items_label(self):
        items_text = ""
        total_amount = 0.0

        for item, details in self.selected_items.items():
            items_text += f"{item} x{details['quantity']} (${details['price']:.2f})\n"
            total_amount += details["price"] * details["quantity"]

        self.selected_items_label.config(text=items_text)
        self.total_amount.set(f"${total_amount:.2f}")

    def generate_bill(self):
        # Here, you can implement the logic to save the bill, print it, or perform any other actions.
        print("Generating Bill...")
        print("Selected Items:")
        for item, details in self.selected_items.items():
            print(f"{item} x{details['quantity']} (${details['price']:.2f})")
        print(f"Total Amount: ${self.total_amount.get():.2f}")
        print("Bill generated successfully!")


if __name__ == "__main__":
    root = tk.Tk()
    billing_system = BillingSystem(root)
    root.mainloop()
