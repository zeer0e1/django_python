from django.urls import path
from home import views as home_view

urlpatterns = [
    path('', home_view.index),
]
