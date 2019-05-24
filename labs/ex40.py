class Song(object): 

    def __init__(self, lyrics): 
        self.lyrics = lyrics 

    def sing_me_a_song(self): 
        for line in self.lyrics: 
            print(line) 
            print('-' * 25) 

happy_bday = Song(["Happy birthday to you", 
                   "I don't want to get sued", 
                   "So I'll stop you right there"]) 

caramelldansen = Song(["Dansa med oss", 
                       "Klappa era hnder", 
                       "Gr som vi gr", 
                       "Ta ngra steg t vnster", 
                       "Lyssna och lr", 
                       "Missa inte chansen", 
                       "Nu are vi hr med", 
                       "Caramelldansen", 
                       "O-o-oa-oa"]) 

bulls_on_parade = Song(["They rally around the family", 
                        "With pockets full of shells"]) 

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

caramelldansen.sing_me_a_song()
