from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Art, Review, Like, UserProfile
from .forms import ReviewForm, ArtForm

class TestArtworkViews(TestCase):

    def setUp(self):
        """Set up for tests. Creates a user, artist profile and a piece of art."""
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.profile = UserProfile.objects.create(
            user=self.user,
            display_name='Test User',
            role='AR'
        )
        self.art = Art.objects.create(
            title='Test Art',
            slug='test-art',
            artist=self.profile,
            about='This is a test art.',
            price=100.00,
            year=2020,
            condition=0,
            status=1
        )
        self.art_list_url = reverse('home')
        self.art_detail_url = reverse('art_details', args=['test-art'])

    def test_art_list_GET(self):
        """Test to verify that a GET request to the art list view returns a 200 status code and uses the correct template."""
        response = self.client.get(self.art_list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'artwork/index.html')

    def test_art_detail_GET(self):
        """Test to verify that a GET request to the art detail view returns a 200 status code and uses the correct template."""
        response = self.client.get(self.art_detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'artwork/art_detail.html')

    def test_like_artwork_POST(self):
        """Test to verify that a POST request to the like artwork view returns a 302 status code (indicating a redirect) and creates a Like object."""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('like_artwork', args=['test-art']))

        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        self.assertTrue(Like.objects.filter(user=self.profile, art=self.art).exists())

    def test_create_advert_POST(self):
        """Test to verify that a POST request to the create advert view returns a 302 status code (indicating a redirect) and creates an Art object."""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('create_advert'), {
            'title': 'New Art',
            'about': 'This is a new art.',
            'price': 200.00,
            'year': 2021,
            'condition': 0
        })

        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        self.assertTrue(Art.objects.filter(title='New Art').exists())