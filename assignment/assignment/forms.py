from django import forms

from assignment import percents


class CalculationForm(forms.Form):
    quantity = forms.IntegerField(min_value=0, label='Quantity of items')
    price = forms.DecimalField(
        min_value=0, decimal_places=2, label='Price per item',
    )
    state = forms.ChoiceField(choices=[(state, state) for state, _ in percents.TAXES])
