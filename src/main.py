"""Main application entry point."""
from utils import load_config
from models.user import User
from models.product import Product
from models.order import Order


def main():
    config = load_config()
    print(f"Starting app with config: {config['app_name']}")
    users = User.load_all()
    products = Product.load_all()
    print(f"Loaded {len(users)} users and {len(products)} products")


if __name__ == "__main__":
    main()
