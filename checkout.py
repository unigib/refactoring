"""A working checkout application in need of refactoring.

All monetary amounts are integer cents.
"""


def calculate_order(items, customer_type, coupon, fulfillment):
    if not isinstance(items, list) or not items:
        raise ValueError("items must be a non-empty list")
    for item in items:
        if not isinstance(item, dict):
            raise ValueError("each item must be a dictionary")
        if not isinstance(item.get("name"), str) or not item["name"]:
            raise ValueError("each item must have a name")
        if type(item.get("price_cents")) is not int or item["price_cents"] < 0:
            raise ValueError("price_cents must be a non-negative integer")
        if type(item.get("quantity")) is not int or item["quantity"] <= 0:
            raise ValueError("quantity must be a positive integer")
    if customer_type not in ("regular", "vip"):
        raise ValueError("unknown customer type")
    if coupon not in (None, "SAVE5"):
        raise ValueError("unknown coupon")
    if fulfillment == "standard":
        return calculate_standard_order(items, customer_type, coupon)
    if fulfillment == "express":
        return calculate_express_order(items, customer_type, coupon)
    if fulfillment == "pickup":
        return calculate_pickup_order(items, customer_type, coupon)
    raise ValueError("unknown fulfillment method")


def calculate_standard_order(items, customer_type, coupon):
    subtotal = 0
    for item in items:
        subtotal = subtotal + item["price_cents"] * item["quantity"]

    customer_discount = 0
    if customer_type == "vip":
        customer_discount = subtotal * 10 // 100
    coupon_discount = 0
    if coupon == "SAVE5":
        if subtotal - customer_discount < 500:
            coupon_discount = subtotal - customer_discount
        else:
            coupon_discount = 500
    discount = customer_discount + coupon_discount
    discounted_subtotal = subtotal - discount

    if discounted_subtotal >= 10000:
        shipping = 0
    else:
        shipping = 500
    tax = (discounted_subtotal * 8 + 50) // 100
    total = discounted_subtotal + shipping + tax
    return {
        "subtotal_cents": subtotal,
        "discount_cents": discount,
        "shipping_cents": shipping,
        "tax_cents": tax,
        "total_cents": total,
    }


def calculate_express_order(items, customer_type, coupon):
    subtotal = 0
    for item in items:
        subtotal = subtotal + item["price_cents"] * item["quantity"]

    customer_discount = 0
    if customer_type == "vip":
        customer_discount = subtotal * 10 // 100
    coupon_discount = 0
    if coupon == "SAVE5":
        if subtotal - customer_discount < 500:
            coupon_discount = subtotal - customer_discount
        else:
            coupon_discount = 500
    discount = customer_discount + coupon_discount
    discounted_subtotal = subtotal - discount

    shipping = 1200
    tax = (discounted_subtotal * 8 + 50) // 100
    total = discounted_subtotal + shipping + tax
    return {
        "subtotal_cents": subtotal,
        "discount_cents": discount,
        "shipping_cents": shipping,
        "tax_cents": tax,
        "total_cents": total,
    }


def calculate_pickup_order(items, customer_type, coupon):
    subtotal = 0
    for item in items:
        subtotal = subtotal + item["price_cents"] * item["quantity"]

    customer_discount = 0
    if customer_type == "vip":
        customer_discount = subtotal * 10 // 100
    coupon_discount = 0
    if coupon == "SAVE5":
        if subtotal - customer_discount < 500:
            coupon_discount = subtotal - customer_discount
        else:
            coupon_discount = 500
    discount = customer_discount + coupon_discount
    discounted_subtotal = subtotal - discount

    shipping = 0
    tax = (discounted_subtotal * 8 + 50) // 100
    total = discounted_subtotal + shipping + tax
    return {
        "subtotal_cents": subtotal,
        "discount_cents": discount,
        "shipping_cents": shipping,
        "tax_cents": tax,
        "total_cents": total,
    }
