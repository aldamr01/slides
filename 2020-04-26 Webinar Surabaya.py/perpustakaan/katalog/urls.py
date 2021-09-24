from django.urls import path, include
from .views import index, create, delete, update

app_name = 'katalog'

urlpatterns = [
    path('', index, name='index'),
    path('create', create, name='create'),
    path('delete/<pk>', delete, name='delete'),
    path('update/<pk>', update, name='update'),
]