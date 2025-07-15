# Lesson 1: Linked Lists - Student Assignment Workbook

## Assignment 1: Basic Linked List Implementation

Complete the missing methods in the LinkedList class below. Test your implementation using the provided test function.

### Your LinkedList Foundation

```python
class Node:
    def __init__(self, data):
        self.data = data    # Store the actual data
        self.next = None    # Pointer to next node
    
    def __str__(self):
        return f"Node({self.data})"

class LinkedList:
    def __init__(self):
        self.head = None    # First node in the list
        self.size = 0       # Number of nodes
    
    def is_empty(self):
        """Check if the list is empty"""
        return self.head is None
    

    
    def append(self, data):
        """Add element to end - ALREADY IMPLEMENTED"""
        new_node = Node(data)   # Create new node
        self.size += 1          # Update count
        
        # Special case: empty list
        if self.head is None:
            self.head = new_node
            return
        
        # Find the last node
        current = self.head
        while current.next:     # Traverse to end
            current = current.next
        current.next = new_node # Link new node
    
    def prepend(self, data):
        """Add element to beginning - ALREADY IMPLEMENTED"""
        new_node = Node(data)       # Create new node
        new_node.next = self.head   # Point to current head
        self.head = new_node        # Update head
        self.size += 1              # Update count
    
    # YOUR IMPLEMENTATIONS START HERE
    
    def get_at_position(self, position):
        """
        Get the data at a specific position (0-indexed)
        
        Args:
            position: Index to retrieve from (0 = first element)
        
        Returns:
            The data at that position
        
        Raises:
            ValueError: If position is out of range
        
        Example:
            ll = LinkedList()
            ll.append("A")
            ll.append("B") 
            ll.get_at_position(1)  # Returns "B"
        """
        # TODO: Implement this method
        # Steps:
        # 1. Check if position is valid (0 <= position < size)
        # 2. Traverse the list 'position' number of times
        # 3. Return the data at that node
        pass
    
    def delete_at_position(self, position):
        """
        Delete the node at a specific position (0-indexed)
        
        Args:
            position: Index to delete from (0 = first element)
        
        Raises:
            ValueError: If position is out of range or list is empty
        
        Example:
            ll = LinkedList()
            ll.append("A")
            ll.append("B")
            ll.append("C")
            ll.delete_at_position(1)  # Removes "B", list becomes A -> C
        """
        # TODO: Implement this method
        # Steps:
        # 1. Check if list is empty
        # 2. Check if position is valid
        # 3. Handle special case: deleting head (position 0)
        # 4. Find the node before the one to delete
        # 5. Update pointers to skip the deleted node
        # 6. Update size
        pass
    


# Test your implementation
def test_basic_linked_list():
    """Test function to verify your LinkedList methods work correctly"""
    print("🧪 Testing Basic LinkedList Implementation...")
    
    # Create and populate list
    ll = LinkedList()
    
    # Build initial list: 0 -> 1 -> 2 -> 3
    ll.append(1)    # List: 1
    ll.append(2)    # List: 1 -> 2
    ll.append(3)    # List: 1 -> 2 -> 3
    ll.prepend(0)   # List: 0 -> 1 -> 2 -> 3
    
    print("List created and populated successfully")
    
    # Test get_at_position
    print("\n--- Testing get_at_position ---")
    try:
        for i in range(4):  # We know we added 4 items
            value = ll.get_at_position(i)
            print(f"Position {i}: {value}")
    except Exception as e:
        print(f"Error in get_at_position: {e}")
    
    # Test delete_at_position
    print("\n--- Testing delete_at_position ---")
    try:
        ll.delete_at_position(1)  # Remove element at position 1
        print("Position 1 deleted successfully")
    except Exception as e:
        print(f"Error in delete_at_position: {e}")
    

    
    print("\n Test completed!")

# Uncomment to test your implementation
# test_basic_linked_list()
```

---

## Assignment 2: Music Playlist Application

Build a music playlist manager using your LinkedList implementation.

### Your Music Player Foundation

```python
class Song:
    def __init__(self, title, artist, duration):
        self.title = title      # Song title
        self.artist = artist    # Artist name
        self.duration = duration  # Duration in seconds
    
    def __str__(self):
        """Format as 'Title by Artist (MM:SS)'"""
        minutes = self.duration // 60
        seconds = self.duration % 60
        return f"{self.title} by {self.artist} ({minutes}:{seconds:02d})"

class MusicPlaylist:
    def __init__(self, name):
        self.name = name
        self.songs = LinkedList()      # Use our LinkedList to store songs
        self.current_position = -1     # Track current song (-1 = not playing)
    
    def add_song(self, title, artist, duration):
        """Add a song to the end of the playlist - ALREADY IMPLEMENTED"""
        song = Song(title, artist, duration)  # Create Song object
        self.songs.append(song)                # Add to linked list
        print(f"Added: {song}")
    
    def display_playlist(self):
        """Show all songs in the playlist - ALREADY IMPLEMENTED"""
        print(f"\nPlaylist: {self.name}")
        print("-" * 60)
        
        if self.songs.is_empty():
            print("No songs in playlist")
            return
        
        # Traverse and display each song
        current = self.songs.head
        position = 0
        
        while current:
           #Displaying data of song currently looping over
            print(f"{position + 1}. {current.data}")
            current = current.next  # Move to next song
            position += 1           # Increment counter
        
        print("-" * 60)
    
    # YOUR IMPLEMENTATIONS START HERE
    
    def play_song_at_position(self, position):
        """
        Start playing the song at the given position (1-indexed for users)
        
        Args:
            position: Song position (1-based, so first song is position 1)
        
        Returns:
            The Song object if successful, None if position is invalid
        
        Example:
            playlist.play_song_at_position(3)  # Play the 3rd song
        """
        # TODO: Implement this method
        # Steps:
        # 1. Check if position is valid (1 <= position <= self.songs.size)
        # 2. Convert to 0-based indexing (subtract 1)
        # 3. Use get_at_position to get the song
        # 4. Update self.current_position
        # 5. Return the song
        pass
    
    def next_song(self):
        """
        Move to and play the next song in the playlist
        
        Returns:
            The next Song object, or None if at end of playlist
        
        Example:
            song = playlist.next_song()
            if song:
                print(f"Now playing: {song}")
        """
        # TODO: Implement this method
        # Steps:
        # 1. Check if we can move to next song (current_position < self.songs.size - 1)
        # 2. Increment current_position
        # 3. Get and return the song at new position
        pass
    
    def previous_song(self):
        """
        Move to and play the previous song in the playlist
        
        Returns:
            The previous Song object, or None if at beginning
        """
        # TODO: Implement this method
        # Steps:
        # 1. Check if we can move to previous song (current_position > 0)
        # 2. Decrement current_position
        # 3. Get and return the song at new position
        pass
    
    def remove_current_song(self):
        """
        Remove the currently playing song from the playlist
        
        Returns:
            True if a song was removed, False if no song is playing
        
        Note: After removal, the next song becomes the current song
        """
        # TODO: Implement this method
        # Steps:
        # 1. Check if a song is currently playing (current_position >= 0)
        # 2. Use delete_at_position to remove the song
        # 3. Adjust current_position (if we removed the last song, go back one)
        # 4. Return True if successful
        pass
    

    
    def find_songs_by_artist(self, artist_name):
        """
        Find all songs by a specific artist
        
        Args:
            artist_name: Name of the artist to search for
        
        Returns:
            List of song titles by that artist
        
        Example:
            queen_songs = playlist.find_songs_by_artist("Queen")
            print(f"Queen songs: {queen_songs}")
        """
        # TODO: Implement this method (BONUS)
        # Steps:
        # 1. Create empty list to store matching song titles
        # 2. Traverse the linked list
        # 3. For each song, check if artist matches (case-insensitive)
        # 4. Add matching song titles to the list
        # 5. Return the list
        pass

# Test your playlist implementation
def test_music_playlist():
    """Test function to verify your MusicPlaylist methods work correctly"""
    print("Testing Music Playlist Implementation...")
    
    # Create a playlist and add songs
    playlist = MusicPlaylist("My Awesome Mix")
    
    # Add test songs (title, artist, duration_in_seconds)
    playlist.add_song("Bohemian Rhapsody", "Queen", 355)        # 5:55
    playlist.add_song("Stairway to Heaven", "Led Zeppelin", 482)  # 8:02
    playlist.add_song("Hotel California", "Eagles", 391)         # 6:31
    playlist.add_song("We Will Rock You", "Queen", 122)         # 2:02
    playlist.add_song("Sweet Child O' Mine", "Guns N' Roses", 356)  # 5:56
    
    # Display initial playlist
    playlist.display_playlist()
    
    # Test playing a specific song
    print("\n--- Testing play_song_at_position ---")
    try:
        song = playlist.play_song_at_position(2)  # Play second song
        if song:
            print(f"Now playing: {song}")
        playlist.display_playlist()
    except Exception as e:
        print(f"Error in play_song_at_position: {e}")
    
    # Test navigation
    print("\n--- Testing next_song ---")
    try:
        next_song = playlist.next_song()
        if next_song:
            print(f"Next song: {next_song}")
        playlist.display_playlist()
    except Exception as e:
        print(f"Error in next_song: {e}")
    
    print("\n--- Testing previous_song ---")
    try:
        prev_song = playlist.previous_song()
        if prev_song:
            print(f"Previous song: {prev_song}")
        playlist.display_playlist()
    except Exception as e:
        print(f"Error in previous_song: {e}")
    
        # Test finding songs by artist (bonus)
    print("\n--- Testing find_songs_by_artist (BONUS) ---")
    try:
        queen_songs = playlist.find_songs_by_artist("Queen")
        print(f"Songs by Queen: {queen_songs}")
    except Exception as e:
        print(f"Error in find_songs_by_artist: {e}")
    
    # Test removing current song
    print("\n--- Testing remove_current_song ---")
    try:
        print(f"Before removal:")
        playlist.display_playlist()
        
        removed = playlist.remove_current_song()
        if removed:
            print("Song removed successfully")
        
        print(f"After removal:")
        playlist.display_playlist()
    except Exception as e:
        print(f"Error in remove_current_song: {e}")
    
    print("\n✅ Test completed!")

# Uncomment to test your implementation
# test_music_playlist()
```

---

## Implementation Tips

### Assignment 1 Hints

1. **get_at_position**: 
   - Check bounds first: `if position < 0 or position >= self.size`
   - Use a loop to traverse `position` number of times
   - Return `current.data` when you reach the target

2. **delete_at_position**:
   - Handle deletion at head separately (position 0)
   - For other positions, find the node BEFORE the one to delete
   - Update pointers to skip the deleted node



### Assignment 2 Hints

1. **play_song_at_position**:
   - Convert from 1-based to 0-based: `zero_based_pos = position - 1`
   - Validate range: `if position < 1 or position > len(self.songs)`

2. **next_song/previous_song**:
   - Check if movement is possible before updating position
   - Handle edge cases (beginning/end of playlist)

3. **remove_current_song**:
   - After deletion, adjust `current_position` if needed
   - If you delete the last song, move position back by 1

---

## Success Criteria

### Assignment 1
- [ ] `get_at_position` correctly retrieves data and handles errors
- [ ] `delete_at_position` removes nodes and updates size properly
- [ ] All test cases pass without errors

### Assignment 2
- [ ] `play_song_at_position` correctly sets current song
- [ ] `next_song` and `previous_song` navigate properly
- [ ] `remove_current_song` deletes and adjusts position
- [ ] **BONUS**: `find_songs_by_artist` returns correct matches

---

## Testing Your Code

After implementing each method, run the test functions to verify your work:

```python
# Test Assignment 1
test_basic_linked_list()

# Test Assignment 2  
test_music_playlist()
```

The test functions will show you exactly what's working and what needs fixing. Use the output to debug your implementations!

Good luck! Remember that linked lists are all about managing pointers correctly. When in doubt, draw the list structure on paper to visualize what should happen. 