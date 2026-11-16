import unittest

from checkout import calculate_order


class CheckoutTests(unittest.TestCase):
    def test_regular_standard_order(self):
        items = [
            {"name": "Book", "price_cents": 2000, "quantity": 2},
            {"name": "Pen", "price_cents": 500, "quantity": 1},
        ]
        self.assertEqual(
            calculate_order(items, "regular", None, "standard"),
            {
                "subtotal_cents": 4500,
                "discount_cents": 0,
                "shipping_cents": 500,
                "tax_cents": 360,
                "total_cents": 5360,
            },
        )

    def test_vip_coupon_and_express_order(self):
        items = [{"name": "Bag", "price_cents": 10000, "quantity": 1}]
        self.assertEqual(
            calculate_order(items, "vip", "SAVE5", "express"),
            {
                "subtotal_cents": 10000,
                "discount_cents": 1500,
                "shipping_cents": 1200,
                "tax_cents": 680,
                "total_cents": 10380,
            },
        )

    def test_pickup_has_no_shipping(self):
        items = [{"name": "Bag", "price_cents": 10000, "quantity": 1}]
        self.assertEqual(
            calculate_order(items, "vip", "SAVE5", "pickup"),
            {
                "subtotal_cents": 10000,
                "discount_cents": 1500,
                "shipping_cents": 0,
                "tax_cents": 680,
                "total_cents": 9180,
            },
        )

    def test_empty_order_is_invalid(self):
        with self.assertRaises(ValueError):
            calculate_order([], "regular", None, "standard")

    def test_unknown_fulfillment_is_invalid(self):
        items = [{"name": "Book", "price_cents": 2000, "quantity": 1}]
        with self.assertRaises(ValueError):
            calculate_order(items, "regular", None, "drone")


if __name__ == "__main__":
    unittest.main()
