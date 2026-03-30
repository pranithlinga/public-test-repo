"""Order model."""
from dataclasses import dataclass
from typing import List
from datetime import datetime


@dataclass
class Order:
    id: int
    user_id: int
    product_id: int
    quantity: int
    total: float
    created_at: str

    @classmethod
    def load_all(cls) -> List["Order"]:
        from utils import read_json
        data = read_json("sample_orders.json")
        return [cls(**item) for item in data]

    @property
    def created_date(self) -> datetime:
        return datetime.fromisoformat(self.created_at)
