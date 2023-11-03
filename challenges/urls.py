from django.urls import path
from . import views


urlpatterns = [
    path("<int:num>", views.month_challenge_by_number),
    path("<str:month>", views.month_challenge, name="url-name"),
    path("", views.index),
]
