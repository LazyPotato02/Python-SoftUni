from .album import Album


class Band:

    def __init__(self, name: str) -> None:
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album.name in [a.name for a in self.albums]:
            return f'Band {self.name} already has {album.name} in their library.'
        else:
            self.albums.append(album)
            return f'Band {self.name} has added their newest album {album.name}.'

    def remove_album(self, album_name: str):
        matches = [a for a in self.albums if a.name == album_name]
        if not matches:
            return f'Album {album_name} is not found.'
        else:
            album = matches[0]
            if album.published:
                return 'Album has been published. It cannot be removed.'
            else:
                self.albums.remove(matches[0])
                return f'Album {matches[0].name} has been removed.'

    def details(self) -> str:
        retval = f'Band {self.name}'
        if self.albums:
            retval += '\n' + '\n'.join([album.details() for album in self.albums])
        return retval