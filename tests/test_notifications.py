import pytest
from src.notifications.notifications import send_email, send_sms, send_push


async def test_send_email():
    result = await send_email("test@example.com", "Hello", "Body")
    assert result["sent"] == True


async def test_send_sms():
    result = await send_sms("+123****7890", "Hello")
    assert result["sent"] == True


async def test_send_push():
    result = await send_push("device123", "Title", "Body")
    assert result["sent"] == True
