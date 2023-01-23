from django.urls import path
from menu_app import views


urlpatterns = [
    path("places/", views.PlaceList.as_view()),
]
