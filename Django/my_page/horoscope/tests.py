from django.test import TestCase
from . import views

# Create your tests here.
class TestHoroscope(TestCase):

    def test_index(self):
        response = self.client.get('/horoscope/')
        self.assertEqual(response.status_code, 200)


    def test_libra_redirect(self):
        response = self.client.get('/horoscope/7/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/horoscope/libra/')

    def test_sings(self):
        for element in views.horoscope_dict.values():
            for sing in element.values():
                response = self.client.get(f'/horoscope/{sing[1]}/')
                self.assertEqual(response.status_code, 200)
                self.assertIn(response.content.decode(), sing[2])

    def test_Horoscope(self):
        for element in views.horoscope_dict.values():
            for sing in element.values():
                response = self.client.get(f'/horoscope/{sing[0]}/')
                self.assertEqual(response.status_code, 302)
                self.assertEqual(response.url, f'/horoscope/{sing[1]}/')







