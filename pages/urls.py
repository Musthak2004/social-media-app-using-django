from django.urls import path
from .views import HomePageView, ProfilePageView, PostPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('profile/<str:username>/', ProfilePageView.as_view(), name='profile'),
    path("post/<int:pk>/", PostPageView.as_view(), name="post"),
]
