from .song import Song


class Album:

    def __init__(self, name: str, *songs) -> None:
        self.name = name
        self.published = False
        self.songs = list(songs)

    def add_song(self, song: Song) -> str:
        if song.name in [s.name for s in self.songs]:
            return 'Song is already in the album.'
        elif self.published:
            return 'Cannot add songs. Album is published.'
        elif song.single:
            return f"Cannot add {song.name}. It's a single"
        else:
            self.songs.append(song)
            return f'Song {song.name} has been added to the album {self.name}.'

    def remove_song(self, song_name: str) -> str:
        if self.published:
            return 'Cannot remove songs. Album is published.'
        elif song_name not in [s.name for s in self.songs]:
            return 'Song is not in the album.'
        else:
            return f'Removed song {song_name} from album {self.name}.'

    def publish(self) -> str:
        if self.published:
            return f'Album {self.name} is already published.'
        else:
            self.published = True
            return f'Album {self.name} has been published.'

    def details(self) -> str:
        retval = f'Album {self.name}'
        if self.songs:
            retval += '\n== ' + '\n== '.join([song.get_info() for song in self.songs])
        return retval