from django.urls import path
from . import views


urlpatterns = [
    path("cities/", views.CityListCreateView.as_view()),
    path("cities/<pk>/", views.CityDetailView.as_view()),
    path("planes/", views.PlaneListCreateView.as_view()),
    path("planes/<pk>/", views.PlaneDetailView.as_view()),
    path("routes/", views.RouteListView.as_view()),
    path("routes/<pk>/", views.RouteDetailDeleteView.as_view()),
    path("find_routes/", views.find_routes, name="find_routes"),
    # path('add_route/', add_route, name="add_route"),
    # path('save_route/', save_route, name="save_route"),
    # path('list/', RouteListView.as_view(), name='list'),
    # path('detail/<int:pk>/', RouteDetailView.as_view(), name='detail'),
    # path('delete/<int:pk>/', RouteDeleteView.as_view(), name='delete'),
    # path('cities/', include(('cities.urls', 'cities'))),
    # path('planes/', include(('planes.urls', 'planes'))),
    # path('accounts/', include(('accounts.urls', 'accounts'))),
    # path('', home, name="home"),
    # path('find_routes/', find_routes, name="find_routes"),
    # path('add_route/', add_route, name="add_route"),
    # path('save_route/', save_route, name="save_route"),
    # path('list/', RouteListView.as_view(), name='list'),
    # path('detail/<int:pk>/', RouteDetailView.as_view(), name='detail'),
    # path('delete/<int:pk>/', RouteDeleteView.as_view(), name='delete'),
]
