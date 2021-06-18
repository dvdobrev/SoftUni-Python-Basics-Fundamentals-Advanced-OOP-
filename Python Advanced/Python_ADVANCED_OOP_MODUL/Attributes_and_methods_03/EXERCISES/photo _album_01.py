class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = []
        for i in range(self.pages):
            self.photos.append([])

    @classmethod
    def from_photos_count(cls, photos_count: int):
        cls.pages = int(photos_count / 4)
        cls.photos = [[] for i in range(cls.pages)]

        return cls

    def add_photo(self, label: str):
        empty_cell = [p for p in self.photos if len(p) < 4]
        if not empty_cell:
            return f"No more free spots"

        for page in range(len(self.photos)):
            if len(self.photos[page]) < 4:
                self.photos[page].append(label)
                return f"{label} photo added successfully on page {page + 1} slot {len(self.photos[page])}"

    def display(self):
        result = ""
        for page in range(len(self.photos)):
            result += "-----------\n"
            result += " ".join(['[]' for i in range(len(self.photos[page]))])

            result += "\n"
        result += "-----------\n"
        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.add_photo("a"))
print(album.add_photo("b"))

print(album.display())

