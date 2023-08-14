from django.urls import path
from web import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/', views.update, name="update"),
    path('display/', views.display, name="display")
]
