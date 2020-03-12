from django.test import TestCase

from assignment import logic, percents


class TestCalculation(TestCase):

    def test_discount(self):
        policy = logic.Discount()
        discounts = sorted(percents.DISCOUNT)
        for prev_i, (bound, percent) in enumerate(discounts[1:]):
            _, prev_percent = discounts[prev_i]

            # in the bound
            self.assertEqual(
                policy.apply(bound+1),
                logic.discount(bound+1, percent),
            )
            # on the bound
            self.assertEqual(
                policy.apply(bound),
                logic.discount(bound, percent),
            )
            # out of the bound
            self.assertEqual(
                policy.apply(bound-1),
                logic.discount(bound-1, prev_percent),
            )

    def test_tax(self):
        total = 10
        for state, percent in percents.TAXES:
            policy = logic.Tax(state)
            self.assertEqual(
                policy.apply(total),
                logic.tax(total, percent),
            )

    def test_calculate(self):
        price, _ = sorted(percents.DISCOUNT)[len(percents.DISCOUNT) // 2]
        state, _ = percents.TAXES[0]
        quantity = 2

        result = logic.calculate(price, quantity, state)
        total = logic.Discount().apply(price * quantity)
        self.assertEqual(result['total']['discounted'], total)

        total = logic.Tax(state).apply(total)
        self.assertEqual(result['total']['tax'], total)
