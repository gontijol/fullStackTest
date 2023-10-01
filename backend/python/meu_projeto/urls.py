from django.urls import path, include
from . import views
from django.contrib import admin
from meu_projeto.views import minha_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dividendos/', include('dividendos.urls')),

]
