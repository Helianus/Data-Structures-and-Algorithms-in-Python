# A doubly linked list 

# Node object
class Node:

    # Initialize the node
    def __init__(self, data):
        self.prev = None # previous node as null
        self.data = data # current node
        self.next = None # next node as null
    
     # Gets data of the node
    def get_Data(self):
        return self.data
    
    # Get the previous data of the node
    def get_Prev(self, prev):
        return self.prev
    
    # Get the next data of the node
    def get_Next(self):
        return self.next
    
    # Set the data of the node
    def set_Data(self, newData):
        self.data = newData
    
    # Set the prev of the node
    def set_Prev(self, newPrev):
        self.prev = newPrev
    
    # Set the next data of the node
    def set_Next(self, newNext):
        self.next = newNext

# Doubly linked list object
class DLinkedList:
    
    # Initialize the head of the doubly linked list
    def __init__(self):
        self.head = None # head as null
        self.size = 0 # length of doubly linked list
    
    # Insert data into the head of the doubly linked list
    def insert_Head(self, data):
        
        # If the head is null, let node to be the head
        # If the head is not null, let node to be the previous one
        # and let original head to be the next node
        if self.head is None: 
            node = Node(data)
            self.head = node
        else:
            node = Node(data)
            node.set_Prev(node)
            node.set_Next(self.head)
            self.head = node
        self.size += 1
        
    # Print the doubly linked list
    def display_list(self):
        curr = self.head
        if curr is None:
            print("This doubly linked list is empty.")
            return False
        while curr:
            print(str(curr.get_Data()), end=" ")
            curr = curr.next

    # Get the size of the linked list
    def get_Size(self):
        return self.size
