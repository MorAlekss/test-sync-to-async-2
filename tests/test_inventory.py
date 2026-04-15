import pytest
from src.inventory.inventory import get_stock, update_stock, reserve_stock, release_stock


def test_get_stock():
    result = get_stock(1)
    assert result["product_id"] == 1
    assert result["quantity"] == 100


def test_update_stock():
    result = update_stock(1, 50)
    assert result["quantity"] == 50
    assert result["updated"] == True


def test_reserve_stock():
    result = reserve_stock(1, 10)
    assert result["reserved"] == 10
    assert result["status"] == "ok"


def test_release_stock():
    result = release_stock(1, 10)
    assert result["released"] == 10
    assert result["status"] == "ok"
