from linkedlist import LinkedList, Node #Importing my LinkedList and Node class from linkedlist.py file


class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration



class MusicPlaylist:
    def __init__(self, name):
        self.name = name
        self.songs = LinkedList()
        self.current_position = -1 #0-based index

    def add_song(self, title, artist, duration):
        song = Song(title, artist, duration)
        self.songs.append(song)

    def display(self):
        """Show all the songs and artists in my playlist"""
        print("========" + self.name+ "==========") 

        current = self.songs.head
        counter = 1
        while current:
            print(f"{counter}.) {current.data.title} - {current.data.artist}")
            current = current.next #Move to the next node in the list
            counter += 1

    def play_song_at_position(self, position): #Takes in 1-based position
        index = position - 1 #converts to 0-based position
        song = self.songs.get_at_position(index) #utilizes our LL method to get_at_postion()
        self.current_position = index
        return song
    
    def next_song(self):
        next_index = self.current_position + 1
        next_song = self.songs.get_at_position(next_index)
        self.current_position = next_index
        return next_song



    
playlist = MusicPlaylist("Bootcamp Bangerz!")
playlist.add_song("Forgotten", "The Plot in You", 175)
playlist.add_song("Blue", "Allen Stone", 180)
playlist.add_song("Belinda Says", "Alvvays", 300)
playlist.add_song("Little Bit Off", "FFDP", 500)
playlist.add_song("Murdergran", "L Cool J", 190)

playlist.display()
selected_song = playlist.play_song_at_position(3)
print(selected_song.title)
print(playlist.current_position)
next_song = playlist.next_song()
print(next_song.title)

    
