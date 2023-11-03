from django.urls import path
from . import views


urlpatterns = [
    path("", views.index,name="index-url"),
    path("<int:num>", views.month_challenge_by_number),
    path("<str:month>", views.month_challenge),
]
