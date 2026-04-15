import pytest
from src.shipping.shipping import create_shipment, track_shipment, cancel_shipment


async def test_create_shipment():
    result = await create_shipment(1, "123 Main St")
    assert result["order_id"] == 1
    assert result["status"] == "created"


async def test_track_shipment():
    result = await track_shipment(1)
    assert result["status"] == "in_transit"


async def test_cancel_shipment():
    result = await cancel_shipment(1)
    assert result["status"] == "cancelled"
