from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Define a URL pattern for the index view
    # Add more URL patterns as needed for other views
]

    