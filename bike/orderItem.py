from dataclasses import dataclass

@dataclass
class OrderItem:
    order_id: int
    item_id: int
    product_id: int
    quantity: int
    list_price: float
    discount: float

    def __hash__(self):
        return hash((self.order_id, self.item_id))

    def __str__(self):
        return f"Item {self.item_id} of Order {self.order_id} – Product {self.product_id}"
