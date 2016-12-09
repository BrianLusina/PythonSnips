class Song(object):
    def __init__(self, lyric):
        self.lyric = lyric

    def sing_me_a_song(self):
        for lyric in self.lyric:
            print(lyric)
