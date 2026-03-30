"""Seed the database with sample data."""
from src.models.user import User
from src.models.product import Product
from src.models.order import Order


def seed():
    users = User.load_all()
    products = Product.load_all()
    orders = Order.load_all()
    print(f"Seeded {len(users)} users, {len(products)} products, {len(orders)} orders")


if __name__ == "__main__":
    seed()
