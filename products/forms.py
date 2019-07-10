"""Formulários"""

from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    """Formulário de Produto"""
    title = forms.CharField(
        label='Titulo',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your title"
                }
            )
        )
    #email = forms.EmailField()
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "new-class-name two",
                "id": "my-id-for-textarea",
                "rows": 20,
                "cols": 100
                }
            )
        )
    price = forms.DecimalField(initial=199.99)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
        ]

    def clean_title(self, *args, **kwargs):
        """ Teste de validação """
        title = self.cleaned_data.get("title")
        if "CFE" in title:
            raise forms.ValidationError("This is not a valid title")
        if "news" in title:
            raise forms.ValidationError("This is not a valid title")
        return title

    def clean_email(self, *args, **kwargs):
        """ Teste de validação """
        email = self.cleaned_data.get("email")
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not a valid email")
        return email

class RawProductForm(forms.Form):
    """Formulário de Produto"""
    title = forms.CharField(
        label='Titulo',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your title"
                }
            )
        )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "new-class-name two",
                "id": "my-id-for-textarea",
                "rows": 20,
                "cols": 100
                }
            )
        )
    price = forms.DecimalField(initial=199.99)
