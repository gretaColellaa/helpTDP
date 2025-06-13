from dataclasses import dataclass

@dataclass
class Customer:
    customer_id: int
    first_name: str
    last_name: str
    phone: str
    email: str
    street: str
    city: str
    state: str
    zip_code: str

    def __hash__(self):
        return hash(self.customer_id)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
