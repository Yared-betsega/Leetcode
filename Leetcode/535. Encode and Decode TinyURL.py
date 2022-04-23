class Codec:
    def __init__(self):
        self.urls = {}
        self.index = 0
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        n = longUrl.find(".com") + 5
        self.urls[self.index] =  longUrl[n:]
        self.index += 1
        return longUrl[:n] + str(self.index - 1)
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return shortUrl[:-1] + self.urls[int(shortUrl[-1])]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
