from django.urls import path, include
from myapp import views

app_name = "myapp"

urlpatterns = [
    path('', views.channel_grid, name='index'),
]