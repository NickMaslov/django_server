from django.urls import path

from . import views


urlpatterns = [
    # Users
    path("users/", views.UserListCreate.as_view()),
    path("users/<pk>/", views.UserDetails.as_view()),
    # Products
    # path("products/", views.ProductList.as_view()),
    path("products/", views.getProducts, name="products"),
    path("products/create/", views.createProduct, name="product-create"),
    path("products/upload/", views.uploadImage, name="image-upload"),
    path("products/<str:pk>/reviews/", views.createProductReview, name="create-review"),
    path("products/top/", views.getTopProducts, name="top-products"),
    path("products/<str:pk>/", views.getProduct, name="product"),
    path("products/update/<str:pk>/", views.updateProduct, name="product-update"),
    path("products/delete/<str:pk>/", views.deleteProduct, name="product-delete"),
    # Orders
    path("orders/", views.getOrders, name="orders"),
    path("orders/add/", views.addOrderItems, name="orders-add"),
    path("orders/myorders/", views.getMyOrders, name="myorders"),
    path(
        "orders/<str:pk>/deliver/", views.updateOrderToDelivered, name="order-delivered"
    ),
    path("orders/<str:pk>/", views.getOrderById, name="user-order"),
    path("orders/<str:pk>/pay/", views.updateOrderToPaid, name="pay"),
]
