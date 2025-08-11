from .inventory import Inventory
from .product import Product

def main():
    """Main function to run the CLI."""
    inventory = Inventory()
    print("Welcome to the Inventory Management System!")

    while True:
        print("\nMenu:")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Update Product Quantity")
        print("4. Get Product Details")
        print("5. View Inventory Summary")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            p_id = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            try:
                price = float(input("Enter Product Price: "))
                quantity = int(input("Enter Product Quantity: "))
                if inventory.add_product(Product(p_id, name, price, quantity)):
                    print("Product added successfully.")
                else:
                    print("Error: Product with this ID already exists.")
            except ValueError:
                print("Invalid price or quantity. Please enter numbers.")

        elif choice == '2':
            p_id = input("Enter Product ID to remove: ")
            if inventory.remove_product(p_id):
                print("Product removed successfully.")
            else:
                print("Error: Product not found.")

        elif choice == '3':
            p_id = input("Enter Product ID to update: ")
            try:
                quantity = int(input("Enter new quantity: "))
                if inventory.update_quantity(p_id, quantity):
                    print("Quantity updated successfully.")
                else:
                    print("Error: Product not found or invalid quantity.")
            except ValueError:
                print("Invalid quantity. Please enter a number.")

        elif choice == '4':
            p_id = input("Enter Product ID to view: ")
            product = inventory.get_product_details(p_id)
            if product:
                print(f"Details: {product}")
            else:
                print("Product not found.")

        elif choice == '5':
            print("\n--- Inventory Summary ---")
            print(inventory.get_inventory_summary())
            print("-------------------------")

        elif choice == '6':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == '__main__':
    main()