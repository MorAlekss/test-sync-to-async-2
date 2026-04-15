import pytest
from src.notifications.notifications import send_email, send_sms, send_push


def test_send_email():
    result = send_email("test@example.com", "Hello", "Body")
    assert result["sent"] == True


def test_send_sms():
    result = send_sms("+1234567890", "Hello")
    assert result["sent"] == True


def test_send_push():
    result = send_push("device123", "Title", "Body")
    assert result["sent"] == True
