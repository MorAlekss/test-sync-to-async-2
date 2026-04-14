import pytest
from src.users.users import get_user, create_user, update_user, delete_user


async def test_get_user():
    result = await get_user(1)
    assert result["id"] == 1
    assert "name" in result


async def test_create_user():
    result = await create_user("Jane", "jane@example.com")
    assert result["name"] == "Jane"


async def test_update_user():
    result = await update_user(1, {"name": "Updated"})
    assert result["id"] == 1
    assert result["name"] == "Updated"


async def test_delete_user():
    result = await delete_user(1)
    assert result["deleted"] == True
