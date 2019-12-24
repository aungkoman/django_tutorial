from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('list', views.list, name='index'),
        path('detail/<int:soldier_id>', views.detail, name='detail'),
]