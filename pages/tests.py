from django.test import SimpleTestCase
from django.urls import reverse

class HomePageTests(SimpleTestCase):

    def test_url_exists_at_correct_location_homepageview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Home')
        self.assertTemplateUsed(response, 'home.html')

class PostPageView(SimpleTestCase):

    def test_url_exists_at_correct_location_postpageview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_postpage_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Post')
        self.assertTemplateUsed(response, "home.html")

class PostCreateView(SimpleTestCase):

    def test_url_exists_at_correct_location_postcreateview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_postcreate_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Post_Create')
        self.assertTemplateUsed(response, "home.html")