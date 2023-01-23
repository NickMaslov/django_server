from django.urls import path
from posts import views


urlpatterns = [
    path("", views.PostList.as_view()),
    path("<int:pk>", views.PostRetrieveDestroy.as_view()),
    path("<int:pk>/vote", views.VoteCreate.as_view()),
]
