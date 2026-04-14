import pytest
from src.orders.orders import get_order, create_order, cancel_order, list_orders


async def test_get_order():
    result = await get_order(1)
    assert result["id"] == 1
    assert result["status"] == "pending"


async def test_create_order():
    result = await create_order(1, ["item1"])
    assert result["user_id"] == 1
    assert result["status"] == "created"


async def test_cancel_order():
    result = await cancel_order(1)
    assert result["status"] == "cancelled"


async def test_list_orders():
    result = await list_orders(1)
    assert isinstance(result, list)
