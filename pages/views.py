from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .models import Profile, Post

User = get_user_model()


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-created_at')
        return context

class PostPageView(TemplateView):
    template_name = "pages/post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_id = self.kwargs.get('pk')
        context['post'] = get_object_or_404(Post, pk=post_id)
        return context

class ProfilePageView(TemplateView):
    template_name = "pages/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.kwargs.get('username')

        user = get_object_or_404(User, username=username)

        profile = get_object_or_404(Profile, user=user)

        context['profile_user'] = user
        context['profile'] = profile

        return context
