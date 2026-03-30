"""Product model."""
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Product:
    id: int
    name: str
    price: float
    category: str
    in_stock: bool

    @classmethod
    def load_all(cls) -> List["Product"]:
        from utils import read_json
        data = read_json("sample_products.json")
        return [cls(**item) for item in data]

    def apply_discount(self, pct: float) -> float:
        return self.price * (1 - pct / 100)
