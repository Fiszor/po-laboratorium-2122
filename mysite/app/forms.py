from dataclasses import field
from django.forms import ModelForm
from .models import Brand

class formBrand(ModelForm):
    class Meta:
        model = Brand
        fields = ['brand_name']