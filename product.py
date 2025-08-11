from dataclasses import dataclass

@dataclass
class Product:
    """A class to represent a single product in the inventory."""
    product_id: str = "Product ID"
    name: str = "Product Name"
    price: float = 15.00
    quantity: int = 100
    