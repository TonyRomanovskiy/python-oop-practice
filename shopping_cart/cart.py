"""Shopping cart module with product management."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    """Immutable product with name, price and stock."""
    name: str
    price: float
    stock: int = 0


class StockError(Exception):
    """Raised when a product is out of stock."""
    pass


class ShoppingCart:
    """Shopping cart that stores products and calculates total price."""

    def __init__(self):
        self._items = []

    def add_product(self, product: Product) -> None:
        """Add a product to the cart. Raise StockError if out of stock."""
        if product.stock == 0:
            raise StockError(f"Товар '{product.name}' отсутствует на складе.")
        self._items.append(product)

    @property
    def total_price(self) -> float:
        """Total price of all products in the cart."""
        return sum(p.price for p in self._items)

    @classmethod
    def from_products(cls, product_list: list) -> "ShoppingCart":
        """Create a cart from a list of products, skipping out-of-stock items."""
        cart = cls()
        for product in product_list:
            if product.stock > 0:
                cart.add_product(product)
        return cart

    def __len__(self) -> int:
        return len(self._items)

    def __str__(self) -> str:
        return f"В вашей корзине {len(self)} товаров на сумму {self.total_price:.2f} руб."