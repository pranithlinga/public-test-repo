"""Tests for model classes."""
import pytest
from src.models.user import User
from src.models.product import Product


def test_user_is_admin():
    admin = User(1, "Alice", "alice@test.com", "admin")
    regular = User(2, "Bob", "bob@test.com", "user")
    assert admin.is_admin()
    assert not regular.is_admin()


def test_product_discount():
    product = Product(1, "Widget", 100.0, "tools", True)
    assert product.apply_discount(10) == 90.0
    assert product.apply_discount(50) == 50.0
