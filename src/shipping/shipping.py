import time


def create_shipment(order_id, address):
    time.sleep(0)
    return {"id": 1, "order_id": order_id, "address": address, "status": "created"}


def track_shipment(shipment_id):
    time.sleep(0)
    return {"id": shipment_id, "status": "in_transit", "location": "warehouse"}


def cancel_shipment(shipment_id):
    time.sleep(0)
    return {"id": shipment_id, "status": "cancelled"}
