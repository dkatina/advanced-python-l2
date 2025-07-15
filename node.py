
class Node:
    def __init__(self, data):
        self.data = data #The cargo of the node
        self.next = None #This links us to the next node in the chain


#Create individual nodes
red = Node('Red')
blue = Node('Blue')
purple = Node('Purple')

# blue -> red -> purple
blue.next = red
red.next = purple

#starting from blue how can I print the color red
print(blue.next.data) #blue.next takes me to the red node, I then need to access the data.

#starting from blue how can I print the color red
print(blue.next.next.data)

black = Node('Black')
green = Node('Green')

purple.next = green
green.next = black

#Traverse my List
print("Traversing the List")
current = red
while current:
    #printing the data of the current node I'm looking at
    print(current.data)
    #Move to the next node
    current = current.next