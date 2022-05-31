from django.urls import path
from .views import index, colaboradores, contato

urlpatterns = [
    path('', index, name='index'),
    path('colaboradores/', colaboradores, name='colaboradores'),
    path('contato/', contato, name='contato')
]