from django.test import TestCase, Client
from .models import Album

class AlbumTest(TestCase):

    #Setup and tear-down function, specific to Django, preps test data.
    @classmethod
    def setUpTestData(cls):
        Album.objects.create(title = "Enter the Wu Tang", artist = "Wu Tang Clan", year = 1993)

    # Test urls
    def test_urls(self):
        # Simulate an http request
        c = Client()
        res = c.get('/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(c.get('/add').status_code, 302)
        self.assertEqual(c.get('/delete').status_code, 302)
        self.assertEqual(c.get('/edit/1').status_code, 200)
    
    def test_model_creation(self):
        #This tests when we make a model
        a = Album.objects.create(title = "Dark Side of the Moon", artist = "Pink Floyd", year = 1973)
        self.assertEqual(a.title,"Dark Side of the Moon")
        self.assertEqual(a.artist, "Pink Floyd")
        self.assertEqual(a.year, 1973)
    
    def test_get_album_model(self):
        # Checking discrete items in database
        # Tests create a temporary junk database that will be deleted after testing.
        # This preserves live model database integrity.
        a = Album.objects.get(id = 1)
        self.assertEqual()
        self.assertEqual(a.id, 1)
        albums = Album.objects.filter(year  = 1993)
        for album in albums:
            self.assertEqual(album.title=="Enter the Wu Tang" or album.title=="I don't know")
    
    def test_view_creation(self):
        c = Client()
        post_data = {
            "title" : "Debut",
            "artist" : "Bjork",
            "year" : 1993
        }
        res = c.post('/add', post_data)
        self.assertEqual(res.status_code, 302)
        a = Album.objects.last()

        self.assertEqual(a.title, post_data['title'])
        self.assertEqual(a.artist, post_data['artist'])
        self.assertEqual(a.year, post_data['year'])
    
    def test_view_edit(self):
        c = Client()
        res = c.get('/edit/1')
        self.assertEqual(res.context['id'], 1)
