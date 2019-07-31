import unittest

from shortener import (
    clear_database,
    get_url,
    set_url,
    working,
    Url,
)


class ShortenerTest(unittest.TestCase):

    def tearDown(self):
        clear_database()

    def test_working(self):
        self.assertEqual(working(), True)

    def test_url_class(self):
        url = Url('http://google.com', 'http://go.to/AAAA')
        self.assertEqual(url.url, 'http://google.com')
        self.assertEqual(url.short_url, "http://go.to/AAAA")

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
        fetched_url = get_url('https://go.to/9999')
        self.assertEqual(fetched_url, 'https://google.com')

    def test_collisions(self):
        set_url('https://google.com')
        url = Url('https://google.com/fakedcollision')
        url.generate_short_url('9999999999999999999999')
        url.save()
        fetched_url = get_url('https://go.to/99999')
        self.assertEqual(fetched_url, 'https://google.com/fakedcollision')
