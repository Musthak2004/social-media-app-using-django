from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "pages/post_create.html"
    fields = ["content", "image"]
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "pages/post_edit.html"
    fields = ["content", "image"]

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.user
    
    def get_success_url(self):
        return reverse_lazy("post", kwargs={"pk": self.object.pk})
    
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "pages/post_delete.html"
    success_url = reverse_lazy("home")

    def get_queryset(self):
        """Only allow the owner to delete their post."""
        return Post.objects.filter(user=self.request.user)
