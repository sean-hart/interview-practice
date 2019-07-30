import unittest

import skel

class Skel(unittest.TestCase):

    def test_working(self):
        self.assertEqual(skel.working(), True)