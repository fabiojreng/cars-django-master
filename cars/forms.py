from django import forms
from cars.models import Car


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"

    def clean_value(self):
        value = self.cleaned_data.get("value")
        if value < 20000:
            self.add_error("value", "Valor mínimo para um carro é de R$20.000")
        return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get("factory_year")
        if factory_year < 2000:
            self.add_error(
                "factory_year",
                "Não é possível inserir carro com ano de fabricação menor que 2000",
            )
        return factory_year

    def clean_model_year(self):
        model_year = self.cleaned_data.get("model_year")
        factory_year = self.cleaned_data.get("factory_year")

        if abs(factory_year - model_year) > 1:
            self.add_error(
                "model_year", "Modelo de carro não compatível com o ano de fabricação"
            )
        return model_year
