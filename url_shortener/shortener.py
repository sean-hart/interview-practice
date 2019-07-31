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

    def save(self):
        urls.append(self)

    def generate_short_url(self, md5=None):
        # Allows us to fake collisions
        if md5 is None:
            md5 = hashlib.md5(self.url.encode("utf-8")).hexdigest()
        identifier = md5[:4]
        short_url = f'{base_domain}{identifier}'
        fetched_url = get_url(short_url)
        if fetched_url and fetched_url == self.url:
            return short_url
        else:
            i = 4
            while self.is_not_unique(short_url):
                identifier = md5[:i]
                short_url = f'{base_domain}{identifier}'
                i += 1
            self.short_url = short_url
            self.save()
            return short_url

    def is_not_unique(self, short_url):
        if get_url(short_url):
            return True
        else:
            return False


def get_url(short_url):
    """
    Fetch the URL from the storage system
    """
    print(urls)
    url_object_list = [x for x in urls if x.short_url == short_url]
    if len(url_object_list) > 1:
        return "More than One"
    elif len(url_object_list) == 0:
        return None
    else:
        return url_object_list[0].url


def set_url(long_url):
    url_object = Url(long_url)
    url_object.generate_short_url()
    return url_object.short_url


def garbage_collection():
    pass


def clear_database():
    urls.clear()
