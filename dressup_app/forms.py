from django import forms
from .models import Item, Outfit

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['type', 'color', 'shape', 'picture']

class OutfitForm(forms.ModelForm):
    class Meta:
        model = Outfit
        fields = ['name', 'items']
