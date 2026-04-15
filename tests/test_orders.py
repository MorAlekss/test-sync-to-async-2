import pytest
from src.orders.orders import get_order, create_order, cancel_order, list_orders


def test_get_order():
    result = get_order(1)
    assert result["id"] == 1
    assert result["status"] == "pending"


def test_create_order():
    result = create_order(1, ["item1"])
    assert result["user_id"] == 1
    assert result["status"] == "created"


def test_cancel_order():
    result = cancel_order(1)
    assert result["status"] == "cancelled"


def test_list_orders():
    result = list_orders(1)
    assert isinstance(result, list)
