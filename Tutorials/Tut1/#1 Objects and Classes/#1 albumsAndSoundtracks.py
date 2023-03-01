"""
Note: since these classes are not private I saw no need to create getters and setters or any methods for most of the
fields
"""

class Album:
    def __init__(self, nameOfAlbum, nameOfArtist, soundTracks=[]):
        self.nameOfAlbum = nameOfAlbum
        self.nameOfArtist = nameOfArtist
        self.soundTracks = soundTracks

    def addSoundTrack(self, song):
        self.soundTracks.append(song)


class SoundTrack:
    def __init__(self, nameOfArtist, nameOfSong, timeDuration, year):
        self.nameOfArtist = nameOfArtist
        self.nameOfSong = nameOfSong
        self.timeDuration = timeDuration
        self.year = year
        self.play = True

    def play(self):
        if not self.play:
            self.play = True

    def pause(self):
        if self.play:
            self.play = False
