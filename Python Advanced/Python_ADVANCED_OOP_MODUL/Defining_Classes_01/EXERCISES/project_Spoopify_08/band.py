from project.song import Song
from project.album import Album

"""
Pay attention to import the correct path!!!!
"""


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        check_valid_album = [a for a in self.albums if a.name == album.name]
        if check_valid_album:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

        # if album.name in map(lambda a: a.name, self.albums):
        #     return f"Band {self.name} already has {album} in their library."
        #
        # self.albums.append(album)
        # return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        check_valid_album = [a for a in self.albums if a.name == album_name]
        if not check_valid_album:
            return f"Album {album_name} is not found."
        is_published = [el for el in check_valid_album if el.published == True]
        if is_published:
            return f"Album has been published. It cannot be removed."
        self.albums = [a for a in self.albums if not a.name == album_name]
        return f"Album {album_name} has been removed."

    def details(self):
        res = f"Band {self.name}\n"
        for album in self.albums:
            res += album.details() + "\n"

        return res


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())
