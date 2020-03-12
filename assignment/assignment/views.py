from django.shortcuts import render

from assignment.forms import CalculationForm
from assignment.logic import calculate


def calculator(request):
    ctx = {}

    if request.method == 'POST':
        form = CalculationForm(request.POST)
        if form.is_valid():
            ctx.update(calculate(**form.cleaned_data))
    else:
        form = CalculationForm()

    ctx['form'] = form
    return render(request, 'index.html', ctx)
