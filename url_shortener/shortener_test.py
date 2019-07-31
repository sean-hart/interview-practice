import unittest

from shortener import (
    clear_database,
    get_url,
    set_url,
    working,
    Url,
    urls,
)


class ShortenerTest(unittest.TestCase):

    def tearDown(self):
        clear_database()

    def test_working(self):
        self.assertEqual(working(), True)

    def test_url_class(self):
        url = Url('https://google.com', 'https://go.to/AAAA')
        self.assertEqual(url.url, 'https://google.com')
        self.assertEqual(url.short_url, "https://go.to/AAAA")

    def test_set_url(self):
        url = set_url('https://google.com')

        self.assertEqual(url, 'https://go.to/9999')

    def test_get_url(self):
        set_url('https://google.com')
        fetched_url = get_url('https://go.to/9999')
        self.assertEqual(fetched_url, 'https://google.com')

    def test_duplicates(self):
        set_url('https://google.com')
        set_url('https://google.com')

        # What it would save if it wasn't a duplicate, but a collision
        fetched_url = get_url('https://go.to/99999')
        self.assertEqual(fetched_url, None)

        # The first one still works
        second_fetched_url = get_url('https://go.to/9999')
        self.assertEqual(second_fetched_url, 'https://google.com')
       
        #there should be only one... 
        self.assertEqual(len(urls), 1)

    def test_collisions(self):
        set_url('https://google.com')
        url = Url('https://google.com/fakedcollision')
        url.generate_short_url('9999999999999999999999')
        fetched_url = get_url('https://go.to/99999')
        self.assertEqual(fetched_url, 'https://google.com/fakedcollision')
