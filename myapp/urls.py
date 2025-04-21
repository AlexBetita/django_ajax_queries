from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.tag_form, name='tag_form'),
]