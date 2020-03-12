from django.shortcuts import render

from assignment.forms import CalculationForm
from assignment.logic import calculate


def calculator(request):
    ctx = {}

    form = CalculationForm()
    ctx['form'] = form
    return render(request, 'index.html', ctx)
