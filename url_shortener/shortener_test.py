import unittest

import shortener

class ShortenerTest(unittest.TestCase):

    def test_working(self):
        self.assertEqual(shortener.working(), True)