"""User model."""
from dataclasses import dataclass
from typing import List


@dataclass
class User:
    id: int
    name: str
    email: str
    role: str

    @classmethod
    def load_all(cls) -> List["User"]:
        from utils import read_csv
        rows = read_csv("sample_users.csv")
        return [cls(int(r["id"]), r["name"], r["email"], r["role"]) for r in rows]

    def is_admin(self) -> bool:
        return self.role == "admin"
