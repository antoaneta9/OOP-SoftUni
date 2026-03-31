from project.song import Song

class Album:
    def __init__(self, name: str, *songs: Song):
        self.name = name
        self.published = False
        self.songs = list(songs) 
    
    def add_song(self, song: Song):
        if self.published:
            return f"Cannot add songs. Album is published."
        
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if song not in self.songs and self.published == False and song.single == False:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."
        if song in self.songs:
            return f"Song is already in the album."
    
    def remove_song(self, song_name: str):
        if self.published:
            return 'Cannot remove songs. Album is published.'
        for song in self.songs:
            if song.name == song_name:
                self.songs.remove(song)
                return f"Removed song {song_name} from album {self.name}."
            
        return 'Song is not in the album.'
    
    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        if self.published:
            return f"Album {self.name} is already published."
    
    def details(self):
        result = [f"Album {self.name}"]
        for song in self.songs:
            result.append(f"== {song.get_info()}")
        return '\n'.join(result)
