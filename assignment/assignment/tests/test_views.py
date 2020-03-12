from django.test import TestCase

from assignment import logic, percents
from assignment.forms import CalculationForm


class TestTomCalculator(TestCase):

    def test_form_presence(self):
        self.assertContains(self.client.get('/'), CalculationForm())
