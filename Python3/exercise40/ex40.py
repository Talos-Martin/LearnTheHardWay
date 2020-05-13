class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    def hello(self):
        print("Hello!")

text = "Happy Birthday to you", "I don't want to get sued", "so I'll stop right here"
happy_bday = Song(text)


bulls_on_parade = Song(["They rally 'round the family", "with pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

bulls_on_parade.hello()


