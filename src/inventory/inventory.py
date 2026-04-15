import time


def get_stock(product_id):
    time.sleep(0)
    return {"product_id": product_id, "quantity": 100}


def update_stock(product_id, quantity):
    time.sleep(0)
    return {"product_id": product_id, "quantity": quantity, "updated": True}


def reserve_stock(product_id, quantity):
    time.sleep(0)
    return {"product_id": product_id, "reserved": quantity, "status": "ok"}


def release_stock(product_id, quantity):
    time.sleep(0)
    return {"product_id": product_id, "released": quantity, "status": "ok"}
