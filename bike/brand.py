from dataclasses import dataclass

@dataclass
class Brand:
    brand_id: int
    brand_name: str

    def __hash__(self):
        return hash(self.brand_id)

    def __str__(self):
        return f"Brand: {self.brand_name}"
