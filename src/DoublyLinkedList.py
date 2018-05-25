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
    def get_Prev(self):
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
        self.tail = None # tail as null
        self.size = 0 # length of doubly linked list
    
    # Insert data into the head of the doubly linked list
    def insert_Head(self, data):
        
        # If the head is null, let node to be the head
        # If the head is not null, let node to be the previous one
        # and let original head to be the next node
        node = Node(data)

        if self.head is None: 
            self.head = node
            self.tail = node
        else:
            self.head.set_Prev(node)
            node.set_Next(self.head)
            self.head = node
        self.size += 1
        
    # Print the doubly linked list
    def display_list(self):
        lst = self.head
        if lst is None:
            print("This doubly linked list is empty.")
            return False
        while lst:
            print(str(lst.get_Data()), end=" ")
            lst = lst.next

    # Get the size of the linked list
    # size will be called in insert functions automatically
    # the time complexity is O(1)
    def get_Size(self):
        return self.size

    # Insert data into the tail of the doubly linked list
    def insert_Tail(self, data):
        node = Node(data)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.set_Next(node)
            node.set_Prev(self.tail)
            self.tail = node
        self.size += 1
    
    # Delete the given item in the linked list
    def delete_Item(self, item):
        lst = self.head # start with the head
        pre = lst.get_Prev() # the previous node
        isFound = False # boolean to remember if we located the item
        while not isFound:
            if lst.get_Data() == item: # if it located, isFound = true
                isFound = True
            else:
                pre = lst # let pre moving into the current node
                lst = lst.get_Next() # let lst moving into the next node
       # If the previous node is null
        if pre is None:
            self.head = lst.get_Next() # Moving head into next node
        else:
            pre.set_Next(lst.get_Next()) # Linked the next node to the previous one (ignore the current node)
        self.size -= 1    
         
    # Reverse the doubly linked list and finally display it
    def reverse_List(self):
        
        # Swap the head and tail
        temp = self.head # store the head of the list
        self.head = self.tail # swap head and tail
        self.tail = temp
        lst = self.head # current node as head

        # Swap each node's prev and next
        while lst is not None:
            prevTemp = lst.get_Prev()
            lst.set_Prev(lst.get_Next())
            lst.set_Next(prevTemp)
            lst = lst.get_Next() # keep going
        
        self.display_list()