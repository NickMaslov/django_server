from django.urls import path
from . import views


urlpatterns = [
    path("cities/", views.CityList.as_view()),
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
