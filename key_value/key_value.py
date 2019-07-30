import hashlib

def working():
    return True

cached_items = []


class CacheObject(object):
    """
    An object to hold Cached Things
    
    Attributes:
        Key: a hash of the value, can be set by hand, but not advised
        Value: supplied when creating calling the set method
    """
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

    def __repr__(self):
        return f'Key: {self.key}, Value: {self.value}'

def get_object(key):
    """ 
    Fetch an item from the cache 
        key: String
    """
    fetched_objects = [x for x in cached_items if x.key == key]
    if len(fetched_objects) == 1:
        return fetched_objects[0]
    elif len(fetched_objects) > 1:
        raise TypeError
    else:
        return None

def set_object(value):
    """ 
    Set a value in cache
        value: String
    """
    key = hashlib.sha256(value.encode('utf-8')).hexdigest()
    fetched_object = get_object(key)
    if fetched_object == None:
        obj = CacheObject(key, value)
        cached_items.append(obj)
        # print(obj.key)
        return obj
    else:
        return fetched_object

def __main__():
    obj = set_object(value='stuff')
    print(obj)

if __name__ == '__main__':
    __main__()