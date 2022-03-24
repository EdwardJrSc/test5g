
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form_create_articule/', include('formArticulos.urls', namespace ='form'))
]
