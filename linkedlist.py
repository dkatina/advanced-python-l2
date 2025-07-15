class Node:
    def __init__(self, data):
        self.data = data #The cargo of the node
        self.next = None #This links us to the next node in the chain




class LinkedList:
    def __init__(self):
        self.head = None #Keeps track of the begining of the chain, If I know where the chain starts I can find anything in the chain

    
    def is_empty(self):
        """Check if we have any nodes"""
        return self.head is None #Returns True or False depending if the Head has a Node or is None
    
    #Adding nodes to the end of the list
    def append(self, data):
        new_node = Node(data)

        if self.is_empty(): #Checking if the list is empty
            self.head = new_node #If list is empty set the new_node as the head of the list
            return #This will break me out of the function
        
        current = self.head #Start at the beginning of the chain 
        while current.next: #Checking if there is a next node
            current = current.next #If there is, then I'll move over to the next node
        
        #Once the while loop finishes current should be a node, with nothing coming next (aka the end)
        current.next = new_node


    def traverse(self):
        print("==========List Contents=============")
        if self.is_empty():
            return "Sorry list is empty"
        
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def insert_at_position(self, position, data):
        """adding a node at a position (0-index)"""
        new_node = Node(data) #create new node

        current = self.head #Starting from the front of the list
        counter = 0
        while counter < position - 1: #Traverse down the list to the object just in-front of the position we want to add to
            current = current.next
            counter += 1

        new_node.next = current.next #New Node points to currents.next node
        current.next = new_node #Current Node points to new node




songs = LinkedList()
print(songs.is_empty())

songs.append("Blue")
songs.append("Twisting Fingers")
songs.append("Baby Shark")
songs.append("Nothing Else Matters")
songs.append("Enter Sandman")
songs.append("Smurf Theme")
songs.append("Chill Beats")

songs.traverse()

songs.insert_at_position(2,"Orange Blossoms")

songs.traverse()
