from django.shortcuts import render
# Create your views here.

from django.views.generic.base import TemplateView

# payments/views.py

class PaymentsPageView(TemplateView):
    template_name = 'payments.html'