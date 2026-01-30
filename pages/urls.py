from django.urls import path
from .views import HomePageView, PostPageView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("post/<int:pk>/", PostPageView.as_view(), name="post"),
    path("post/create/", PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/edit/", PostUpdateView.as_view(), name="post_update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
]
