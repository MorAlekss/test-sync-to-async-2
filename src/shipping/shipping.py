import asyncio


async def create_shipment(order_id, address):
    await asyncio.sleep(0)
    return {"id": 1, "order_id": order_id, "address": address, "status": "created"}


async def track_shipment(shipment_id):
    await asyncio.sleep(0)
    return {"id": shipment_id, "status": "in_transit", "location": "warehouse"}


async def cancel_shipment(shipment_id):
    await asyncio.sleep(0)
    return {"id": shipment_id, "status": "cancelled"}
