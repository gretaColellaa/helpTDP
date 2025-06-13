from dataclasses import dataclass

@dataclass
class Stock:
    store_id: int
    product_id: int
    quantity: int

    def __hash__(self):
        return hash((self.store_id, self.product_id))

    def __str__(self):
        return f"Stock: Store {self.store_id} – Product {self.product_id} – Qty {self.quantity}"
