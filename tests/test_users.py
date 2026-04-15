import pytest
from src.users.users import get_user, create_user, update_user, delete_user


def test_get_user():
    result = get_user(1)
    assert result["id"] == 1
    assert "name" in result


def test_create_user():
    result = create_user("Jane", "jane@example.com")
    assert result["name"] == "Jane"


def test_update_user():
    result = update_user(1, {"name": "Updated"})
    assert result["id"] == 1
    assert result["name"] == "Updated"


def test_delete_user():
    result = delete_user(1)
    assert result["deleted"] == True
