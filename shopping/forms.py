from django import forms
from shopping.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model= Product
        fields='__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Введите название товара'
                }
            ),
            'description': forms.TextInput (
                attrs={
                    'class': 'form-control',
                    'placeholder':'Введите описание товара'
                }
            ),
            'price':forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Введите цену'
                }
            ),
            'discount': forms.NumberInput (
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите скидку'
                }
            ),
            'category':forms.Select(
                attrs={
                    'class':'form-control',

                }
            ),
            'tags':forms.SelectMultiple(
                attrs={
                    'class':'form-control'
                }
            )
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100,min_length=3,
                               widget=forms.TextInput(
                                   attrs={
                                       'class':'form-control'
                                   }
                               ))
    password = forms.CharField(max_length=100,min_length=3,
                               widget=forms.PasswordInput(
                                   attrs={
                                       'class':'form-control'
                                   }
                               ))
