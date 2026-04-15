import pytest
from src.shipping.shipping import create_shipment, track_shipment, cancel_shipment


def test_create_shipment():
    result = create_shipment(1, "123 Main St")
    assert result["order_id"] == 1
    assert result["status"] == "created"


def test_track_shipment():
    result = track_shipment(1)
    assert result["status"] == "in_transit"


def test_cancel_shipment():
    result = cancel_shipment(1)
    assert result["status"] == "cancelled"
