from django.urls import path
from .views import formArticulo

app_name="form"

urlpatterns = [
    path('form/',formArticulo.as_view(), name = 'form')
]