from dataclasses import dataclass

@dataclass
class Order:
    order_id: int
    customer_id: int
    order_status: int
    order_date: str
    required_date: str
    shipped_date: str
    store_id: int
    staff_id: int

    def __hash__(self):
        return hash(self.order_id)

    def __str__(self):
        return f"Order {self.order_id} – Customer {self.customer_id}"
