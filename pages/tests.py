from django.test import SimpleTestCase
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from pages.models import Post 

User = get_user_model()

class HomePageTests(SimpleTestCase):

    def test_url_exists_at_correct_location_homepageview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Home')
        self.assertTemplateUsed(response, 'home.html')
        
class PostPageViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="nanba",
            password="test123"
        )

        self.post = Post.objects.create(
            user=self.user,
            content="Test Post Content"
        )

    def test_post_url_exists(self):
        response = self.client.get(f"/post/{self.post.pk}/")
        self.assertEqual(response.status_code, 200)

    def test_post_view_uses_correct_template(self):
        response = self.client.get(
            reverse("post", kwargs={"pk": self.post.pk})
        )
        self.assertTemplateUsed(response, "pages/post.html")

    def test_post_content_displayed(self):
        response = self.client.get(
            reverse("post", kwargs={"pk": self.post.pk})
        )
        self.assertContains(response, "Test Post Content")


class PostCreateViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="creator",
            password="test123"
        )
        self.client.login(username="creator", password="test123")

    def test_post_create_page_status_code(self):
        response = self.client.get(reverse("post_create"))
        self.assertEqual(response.status_code, 200)

    def test_post_create_template_used(self):
        response = self.client.get(reverse("post_create"))
        self.assertTemplateUsed(response, "pages/post_create.html")

    def test_create_post(self):
        response = self.client.post(
            reverse("post_create"),
            {
                "content": "New Post From Test"
            }
        )
        self.assertEqual(Post.objects.count(), 1)
        self.assertContains(
            self.client.get(reverse("home")),
            "New Post From Test"
        )
