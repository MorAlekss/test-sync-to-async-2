import asyncio


async def get_stock(product_id):
    await asyncio.sleep(0)
    return {"product_id": product_id, "quantity": 100}


async def update_stock(product_id, quantity):
    await asyncio.sleep(0)
    return {"product_id": product_id, "quantity": quantity, "updated": True}


async def reserve_stock(product_id, quantity):
    await asyncio.sleep(0)
    return {"product_id": product_id, "reserved": quantity, "status": "ok"}


async def release_stock(product_id, quantity):
    await asyncio.sleep(0)
    return {"product_id": product_id, "released": quantity, "status": "ok"}
