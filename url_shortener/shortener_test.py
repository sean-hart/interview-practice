import unittest

from shortener import(
    get_url,
    set_url,
    working,
    Url,
) 

class ShortenerTest(unittest.TestCase):

    def test_working(self):
        self.assertEqual(working(), True)

    def test_url_class(self):
        url = Url('http://google.com', 'http://go.to/AAAA')
        self.assertEqual(url.url, 'http://google.com')
        self.assertEqual(url.short_url, "http://go.to/AAAA")

    def test_set_url(self):
        url = set_url('https://google.com')
        self.assertEqual(url.short_url, 'https://go.to/9999' )

    def test_get_url(self):
        set_url('https://google.com')
        fetched_url = get_url('https://go.to/9999')
        self.assertEqual(fetched_url.url, 'https://google.com')
        
        