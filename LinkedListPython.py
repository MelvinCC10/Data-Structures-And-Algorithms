""" Linked List Data Structure in Python """

class Node():

    def __init__(self,data,next = None):
        self.data = data
        self.next = next

class LinkedList():

    def __init__(self):
        self.len = 0
        self.head = None
        self.tail = None

    def append(self, data, next = None):
        """ Adds a Node to the end of the linked list"""
        if self.head == None:           # The first Node to be created is the head
            self.head = Node(data)
            self.tail = self.head
            len += 1
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
            len += 1

class DoublyNode():

    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList():

    def __init__(self):
        self.len = 0
        self.head = None
        self.tail = None

    def append(self, data):
        """ Adds a Node to the end of the linked list"""
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
            self.len += 1
        else:
            self.tail.next = Node(data)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
            self.len += 1




""" Example """

# creating a Doubly Linked List
linked_list = DoublyLinkedList()
for i in range(10):
    linked_list.append(i)

# Traverse Forward
traverse_point = linked_list.head
while traverse_point.next:
    print(str(traverse_point.data))
    traverse_point = traverse_point.next
print(str(traverse_point.data))
print("\n")

# Traverse Backwards
while traverse_point.prev:
    print(str(traverse_point.data))
    traverse_point = traverse_point.prev
print(str(traverse_point.data))
