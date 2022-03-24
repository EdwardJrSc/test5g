from django import forms

class formArticulo(forms.Form):
    nombreArticulo = forms.CharField(label = 'Nombre', max_length = 50)
    valorArticulo = forms.IntegerField(label = 'Valor')

