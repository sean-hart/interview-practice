import hashlib


def working():
    return True


base_domain = 'https://go.to/'
urls = []


class Url(object):
    """
    An Object to store data for urls
        Attributes:
            url: String
            short_url: String
            ttl: Integer (seconds until expire)
            create_time: DateTime
    """

    def __init__(self, url=None, short_url=None, ttl=60):
        self.url = url
        self.short_url = short_url
        self.ttl = ttl

    def __repr__(self):
        return(
            f"ShortURL: {self.short_url}, FullURL: {self.url}, TTL: {self.ttl}"
        )


def get_url(short_url):
    """
    Fetch the URL from the storage system
    """
    print(urls)
    url_object_list = [x for x in urls if x.short_url == short_url]
    if len(url_object_list) > 1:
        return "More than One"
    elif len(url_object_list) == 0:
        return ""
    else:
        return url_object_list[0].url


def set_url(long_url):
    # Let's grab the first 4 characters of an mmd5 hash as an identifier
    identifier = hashlib.md5(long_url.encode("utf-8")).hexdigest()[:4]
    short_url = f'{base_domain}{identifier}'
    url_object = Url(long_url, short_url)
    urls.append(url_object)
    return url_object


def garbage_collection():
    pass


def clear_database():
    urls.clear()
