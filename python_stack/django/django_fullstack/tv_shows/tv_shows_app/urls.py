from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.index),
    path('shows/new', views.index),
    path('shows/create', views.index),
    path('shows/<id>', views.index),
    path('shows/<id>/edit', views.index),
    path('shows/<id>/update', views.index),
    path('shows/<id>/destroy', views.index),
]