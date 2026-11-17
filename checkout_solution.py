"""One possible refactoring of the checkout exercise.

All monetary amounts are integer cents.
"""

VIP_DISCOUNT_PERCENT = 10
COUPON_DISCOUNT_CENTS = 500
FREE_STANDARD_SHIPPING_THRESHOLD_CENTS = 10000
STANDARD_SHIPPING_CENTS = 500
EXPRESS_SHIPPING_CENTS = 1200
TAX_PERCENT = 8
PERCENT = 100


def calculate_order(items, customer_type, coupon, fulfillment):
    """Calculate an order without changing the caller's items."""
    _validate_order(items, customer_type, coupon, fulfillment)

    subtotal = sum(item["price_cents"] * item["quantity"] for item in items)
    discount = _calculate_discount(subtotal, customer_type, coupon)
    discounted_subtotal = subtotal - discount
    shipping = _calculate_shipping(discounted_subtotal, fulfillment)

    # Integer arithmetic rounds tax to the nearest cent, with half cents up.
    tax = (discounted_subtotal * TAX_PERCENT + PERCENT // 2) // PERCENT
    return {
        "subtotal_cents": subtotal,
        "discount_cents": discount,
        "shipping_cents": shipping,
        "tax_cents": tax,
        "total_cents": discounted_subtotal + shipping + tax,
    }


def _validate_order(items, customer_type, coupon, fulfillment):
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
    if fulfillment not in ("standard", "express", "pickup"):
        raise ValueError("unknown fulfillment method")


def _calculate_discount(subtotal, customer_type, coupon):
    customer_discount = 0
    if customer_type == "vip":
        customer_discount = subtotal * VIP_DISCOUNT_PERCENT // PERCENT

    coupon_discount = 0
    if coupon == "SAVE5":
        coupon_discount = min(subtotal - customer_discount, COUPON_DISCOUNT_CENTS)
    return customer_discount + coupon_discount


def _calculate_shipping(discounted_subtotal, fulfillment):
    if fulfillment == "standard":
        if discounted_subtotal >= FREE_STANDARD_SHIPPING_THRESHOLD_CENTS:
            return 0
        return STANDARD_SHIPPING_CENTS
    if fulfillment == "express":
        return EXPRESS_SHIPPING_CENTS
    return 0  # Pickup; fulfillment was already validated.
