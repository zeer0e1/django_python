from django.urls import path
from blog import views as blog_view

urlpatterns = [
    path('', blog_view.blog),
    path('exemplo/', blog_view.exemplo)

]
