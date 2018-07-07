from django.urls import path

from . import views

urlpatterns = [
    path('form-name-view/', views.form_name_view, name='form_name_view'),
    path('', views.index, name='index')
]