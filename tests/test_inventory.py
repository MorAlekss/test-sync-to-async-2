import pytest
from src.inventory.inventory import get_stock, update_stock, reserve_stock, release_stock


async def test_get_stock():
    result = await get_stock(1)
    assert result["product_id"] == 1
    assert result["quantity"] == 100


async def test_update_stock():
    result = await update_stock(1, 50)
    assert result["quantity"] == 50
    assert result["updated"] == True


async def test_reserve_stock():
    result = await reserve_stock(1, 10)
    assert result["reserved"] == 10
    assert result["status"] == "ok"


async def test_release_stock():
    result = await release_stock(1, 10)
    assert result["released"] == 10
    assert result["status"] == "ok"
