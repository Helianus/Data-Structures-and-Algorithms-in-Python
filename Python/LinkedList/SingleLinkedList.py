# A Single Linked list 

# Node object
class Node:

    # Initialize the node
    def __init__(self, data):
        self.data = data # head's data
        self.next = None # next as null
    
    # Gets data of the node
    def get_Data(self):
        return self.data
    
    # Get the next data of the node
    def get_Next(self):
        return self.next
    
    # Set the data of the node
    def set_Data(self, newData):
        self.data = newData
    
    # Set the next data of the node
    def set_Next(self, newNext):
        self.next = newNext


# Linked list object
class LinkedList:
    
    # Initialize the head of linked list
    def __init__(self):
        self.head = None # head as null

    # Insert data into the head of the linkd list
    def insert_head(self, data):
        node = Node(data) # Assign data to node
        node.set_Next(self.head) # Set old head to be next
        self.head = node # Assign new node to be the head of the Node
        del node

    # Print the Linke list
    def display(self):
        lst = self.head # start with the head
        if lst is None: # if the head is none, return False
            print("This linked list is an empty.")
            return False
        while lst:
             print(str(lst.get_Data()), end=" ") # Print the linked
             lst = lst.next # lst as next

    # Get size of the linkd list by traversaling
    def get_Size(self):
        lst = self.head # strat with the head
        count = 0 # count the nodes
        if lst is None:
            print("This linked list is an empty.")
            return False
        while lst:
            count += 1 # traversaling the nodes
            lst = lst.get_Next() # go to next
        return count        

    # Search the linked list by given an item
    def search_Item(self, item):
        lst = self.head # start with the head
        isFound = False # boolean to remember if we located the item
        while lst and not isFound:
            if lst.get_Data() == item: # if it located, isFound = true
                isFound = True 
            else:
                lst = lst.get_Next() # if it is not, go to next
        return isFound

    # Delete the given item in the linked list
    def delete_Item(self, item):
        lst = self.head # start with the head
        pre = None # the previous node
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

    def reverse_List(self):
        prev = None
        curr = self.head
        while curr is not None:
            next = curr.get_Next()
            curr.set_Next(prev)
            prev = curr
            curr = next
        self.head = prev
        self.display()