import math

class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = math.ceil(photos_count / 4)
        return cls(pages)

    def add_photo(self, label: str):
        for i in range(self.pages):
            if len(self.photos[i]) < 4:
                self.photos[i].append(label)
                return f"{label} photo added successfully on page {i + 1} slot {len(self.photos[i])}"
        return "No more free slots"
    def display(self):
        res = []
        for page in self.photos:
            res.append('-'* 11)
            res.append(' '.join('[]' for _ in page))
        res.append('-'* 11)
        return '\n'.join(res)

album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())