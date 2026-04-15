import pytest
from src.payments.payments import process_payment, refund_payment, get_payment_status


def test_process_payment():
    result = process_payment(1, 100.0, "card")
    assert result["status"] == "success"


def test_refund_payment():
    result = refund_payment(1, 50.0)
    assert result["status"] == "refunded"


def test_get_payment_status():
    result = get_payment_status(1)
    assert result["status"] == "success"
