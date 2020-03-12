from django.test import TestCase

from assignment import logic, percents
from assignment.forms import CalculationForm


class TestTomCalculator(TestCase):

    def test_form_presence(self):
        self.assertContains(self.client.get('/'), CalculationForm())

    def test_calculation(self):
        state, percent = percents.TAXES[0]
        resp = self.client.post(
            '/', {'price': 1, 'quantity': 1, 'state': state},
        )

        with_tax = logic.tax(1, percent)
        self.assertEqual(resp.context['total']['discounted'], 1.0)
        self.assertEqual(resp.context['total']['tax'], with_tax)
        self.assertContains(resp, '1.00')
        self.assertContains(resp, with_tax)
