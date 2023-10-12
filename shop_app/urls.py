from django.urls import path
from . import views

urlpatterns = [
    path("client/<int:client_id>/", views.client, name="client"),
    path("client/<int:client_id>/order7", views.client_7days, name="client_7days"),
    path("client/<int:client_id>/order30", views.client_30days, name="client_30days"),
    path("client/<int:client_id>/order365", views.client_365days, name="client_365days"),
]
