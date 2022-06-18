import pandas as pd

from django.shortcuts import render
from django.views import View

from farecalculator.forms import FareCalculatorForm


class FareCalculatorView(View):

    template_name = "farecalculator/fare.html"

    def get(self, request):
        context = {"form": FareCalculatorForm()}
        return render(request, self.template_name, context=context)

    def post(self, request):

        form = FareCalculatorForm(request.POST)

        context = {"form": form}

        if form.is_valid():
            time = form.cleaned_data["time"]
            noon = form.cleaned_data["noon"]
            distance = form.cleaned_data["distance"]

            df = pd.read_csv("faredata.csv")
            wanted_data = df.loc[(df["Time"] == time) & (df["Shift"] == noon)]
            pure_price = wanted_data["Initial Fare"] + distance * wanted_data["Km Rate"]

            price_service = (
                pure_price + pure_price * wanted_data["service charge(%)"] / 100
            )

            final_price = (
                price_service + price_service * wanted_data["Surge Charge(%)"] / 100
            )
            context["price"] = float(round(final_price, 2))

        return render(request, self.template_name, context=context)
