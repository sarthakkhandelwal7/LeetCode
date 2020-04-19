import random
import string


class Codec:

    def __init__(self):
        self.urls = {}

    def encode(self, longUrl):
        suffix = string.ascii_letters + string.digits
        tiny_url = 'http://tinyurl.com/'.join(random.choice(suffix) for _ in range(6))
        self.urls[tiny_url] = longUrl
        return tiny_url

    def decode(self, shortUrl):
        return self.urls[shortUrl]