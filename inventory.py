from typing import Dict, Optional
from .product import Product

class Inventory:
    """Manages a collection of products in the inventory."""

    def __init__(self):
        self._products: Dict[str, Product] = {}
    
    def add_product(self, product: Product) -> bool:
        # TODO: Implement this method.

        # Check if the product ID already exists
        if product.product_id in self._products:
            if product.name != self._products[product.product_id].name:
                print(f"Product ID {product.product_id} already exists with a different name.")
                return False
            # Add the product to the inventory
            self._products[product.product_id].quantity += product.quantity
            # Update the existing product's price if it differs
            if product.price != self._products[product.product_id].price:
                print(f"Product ID {product.product_id} already exists with a different price.")
                self._products[product.product_id].price = product.price
            return True
        else:
            # Add the new product to the inventory
            self._products[product.product_id] = product
            return True

    def remove_product(self, product_id: str) -> bool:
        if product_id in self._products:
            del self._products[product_id]
            return True
        return False
             
    def update_quantity(self, product_id: str, new_quantity: int) -> bool:
        if new_quantity < 0:
            return False
        if product_id in self._products:
            self._products[product_id].quantity = new_quantity
            return True
        return False
        # TODO: Implement this method.
        # If the product exists, update its quantity and return True
        # If the product does not exist or the new quantity is invalid, return False
        # if new_quantity < 0:
        #     return False
        # if product_id in self._products:
        #     self._products[product_id].quantity = new_quantity
        #     return True
        # return False
        # # If the product exists, update its quantity and return True
        # # If the product does not exist or the new quantity is invalid, return False                

    def get_product_details(self, product_id: str) -> Optional[Product]:
        """Returns the details of a product by its ID."""
        return self._products.get(product_id, None)

    def get_inventory_summary(self) -> str:
        """Returns a summary of the inventory."""
        total_products = len(self._products)
        total_quantity = sum(product.quantity for product in self._products.values())
        total_value = sum(product.price * product.quantity for product in self._products.values())
        
        summary_lines = [
            f"Total Products: {total_products}",
            f"Total Quantity: {total_quantity}",
            f"Total Value: {total_value:.2f}"
        ]
        
        for product in self._products.values():
            summary_lines.append(f"{product.product_id}: {product.name}, Price: {product.price}, Quantity: {product.quantity}")
        
        return "\n".join(summary_lines)