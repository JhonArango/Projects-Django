from django import forms
from countries.models import Country

class CountryCreateFormModel(forms.ModelForm):
    """CountryCreateFormModel definition."""
    class Meta:
        model = Country
        fields = ['name', 'code', 'continent']
       