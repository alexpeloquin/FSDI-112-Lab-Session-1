from django.urls import path
from . import views

urlpatterns = [
    path( '', views.index, name='index'),
    path( 'test', views.test, name="test"),
    path( 'contact', views.contact, name="conact"),
    path( 'contactme', views.contact, name="conactme")
]
