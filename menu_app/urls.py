from django.urls import path
from menu_app import views


urlpatterns = [
    # path("auth/", include("djoser.urls")),
    # path("auth/", include("djoser.urls.authtoken")),
    path("places/", views.PlaceList.as_view()),
    path("places/<pk>", views.PlaceDetail.as_view()),
    path("categories/", views.CategoryList.as_view()),
    path("categories/<pk>", views.CategoryDetail.as_view()),
    path("menu_items/", views.MenuItemList.as_view()),
    path("menu_items/<pk>", views.MenuItemDetail.as_view()),
    path("create_payment_intent/", views.create_payment_intent),
    path("orders/", views.OrderList.as_view()),
    path("orders/<pk>", views.OrderDetail.as_view()),
]
