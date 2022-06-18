from django.urls import path
from farecalculator.views import FareCalculatorView

urlpatterns = [
    path('',FareCalculatorView.as_view(),name= "fare-calculator")
]