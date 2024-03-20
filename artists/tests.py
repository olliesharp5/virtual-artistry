from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserProfile
from artwork.models import Art

class TestArtistViews(TestCase):

    def setUp(self):
        """Creates a user, artist profile and art"""
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.artist_profile = UserProfile.objects.create(user=self.user, role='AR', display_name='Test Artist', location='Test Location', about='Test About')
        self.art = Art.objects.create(artist=self.artist_profile, title='Test Art', about='Test About', price=100)

    def test_artist_list_view(self):
        """Verifies get request for artist list"""
        response = self.client.get(reverse('artists'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Artist')

    def test_artist_profile_view(self):
        """Verifies get request for artist profile"""
        response = self.client.get(reverse('artist_profile', args=['testuser']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Artist')
        self.assertContains(response, 'Test Location')
        self.assertContains(response, 'Test About')
        self.assertContains(response, 'Test Art')


