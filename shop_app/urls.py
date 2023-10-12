from django.urls import path
from . import views

urlpatterns = [
    path("client/<int:client_id>/", views.client, name="client"),
    # path("cube/<int:count>", views.cube, name="cube"),
    # path("rand_num/<int:count>", views.rand_num, name="rand_num"),
]
