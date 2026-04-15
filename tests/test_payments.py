import pytest
from src.payments.payments import process_payment, refund_payment, get_payment_status


async def test_process_payment():
    result = await process_payment(1, 100.0, "card")
    assert result["status"] == "success"


async def test_refund_payment():
    result = await refund_payment(1, 50.0)
    assert result["status"] == "refunded"


async def test_get_payment_status():
    result = await get_payment_status(1)
    assert result["status"] == "success"
