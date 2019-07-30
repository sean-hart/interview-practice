import unittest

from key_value import CacheObject, get_object, set_object, working

class KeyValue(unittest.TestCase):

    def test_working(self):
        self.assertEqual(working(), True)

    def test_object(self):
        obj = CacheObject(key='1111', value='stuff')
        self.assertEqual(obj.key, '1111')
        self.assertEqual(obj.value, 'stuff')

    def test_set(self):
        obj = set_object('things')
        self.assertEqual(obj.key, '7e1ddfc85ae45a95330209c0834c59876011aa587be693354cbd1f40bf637fcd')

    def test_get(self):
        set_object('stuffandthings')
        fetched_object = get_object('e7790f388db0963ecad4e4ce79adef1afac3379bc8e1a2bde4a9569bfd5e46aa')
        self.assertEqual(fetched_object.value, 'stuffandthings')

    def test_multiples(self):
        set_object('stuff')
        set_object('stuff')
        fetched_object = get_object('35bafb1ce99aef3ab068afbaabae8f21fd9b9f02d3a9442e364fa92c0b3eeef0') 
        self.assertEqual(fetched_object.value, 'stuff')