import copy
import unittest

from checkout import calculate_order as original_calculate_order
from checkout_solution import calculate_order as solution_calculate_order


class CheckoutContractTests:
    def test_regular_standard_order(self):
        result = self.calculate_order(
            [
                {"name": "Book", "price_cents": 2000, "quantity": 2},
                {"name": "Pen", "price_cents": 500, "quantity": 1},
            ],
            "regular",
            None,
            "standard",
        )
        self.assertEqual(
            result,
            {
                "subtotal_cents": 4500,
                "discount_cents": 0,
                "shipping_cents": 500,
                "tax_cents": 360,
                "total_cents": 5360,
            },
        )

    def test_standard_shipping_threshold_after_coupon(self):
        for price, shipping, total in ((10499, 500, 11299), (10500, 0, 10800)):
            with self.subTest(price=price):
                result = self.calculate_order(
                    [{"name": "Item", "price_cents": price, "quantity": 1}],
                    "regular",
                    "SAVE5",
                    "standard",
                )
                self.assertEqual(result["shipping_cents"], shipping)
                self.assertEqual(result["total_cents"], total)

    def test_vip_coupon_with_express_and_pickup(self):
        items = [{"name": "Bag", "price_cents": 10000, "quantity": 1}]
        for fulfillment, shipping, total in (("express", 1200, 10380), ("pickup", 0, 9180)):
            with self.subTest(fulfillment=fulfillment):
                result = self.calculate_order(items, "vip", "SAVE5", fulfillment)
                self.assertEqual(
                    result,
                    {
                        "subtotal_cents": 10000,
                        "discount_cents": 1500,
                        "shipping_cents": shipping,
                        "tax_cents": 680,
                        "total_cents": total,
                    },
                )

    def test_discount_and_tax_rounding(self):
        vip = self.calculate_order(
            [{"name": "Item", "price_cents": 19, "quantity": 1}],
            "vip",
            None,
            "pickup",
        )
        self.assertEqual(vip["discount_cents"], 1)
        for price, tax in ((6, 0), (7, 1)):
            with self.subTest(price=price):
                result = self.calculate_order(
                    [{"name": "Item", "price_cents": price, "quantity": 1}],
                    "regular",
                    None,
                    "pickup",
                )
                self.assertEqual(result["tax_cents"], tax)

    def test_coupon_cannot_exceed_subtotal(self):
        result = self.calculate_order(
            [{"name": "Item", "price_cents": 300, "quantity": 1}],
            "regular",
            "SAVE5",
            "pickup",
        )
        self.assertEqual(result["discount_cents"], 300)
        self.assertEqual(result["total_cents"], 0)

    def test_invalid_inputs_and_non_mutation(self):
        items = [{"name": "Item", "price_cents": 100, "quantity": 2}]
        original = copy.deepcopy(items)
        self.calculate_order(items, "regular", None, "standard")
        for args in (
            ([], "regular", None, "standard"),
            (
                [{"name": "Item", "price_cents": True, "quantity": 1}],
                "regular",
                None,
                "standard",
            ),
            (items, "unknown", None, "standard"),
            (items, "regular", "unknown", "standard"),
            (items, "regular", None, "unknown"),
        ):
            with self.subTest(args=args), self.assertRaises(ValueError):
                self.calculate_order(*args)
        self.assertEqual(items, original)


class OriginalCheckoutContractTests(CheckoutContractTests, unittest.TestCase):
    calculate_order = staticmethod(original_calculate_order)


class SolutionCheckoutContractTests(CheckoutContractTests, unittest.TestCase):
    calculate_order = staticmethod(solution_calculate_order)


if __name__ == "__main__":
    unittest.main()
