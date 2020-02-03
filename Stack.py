""" Stack Data Structure implemented using a Doubly Linked List """

class Node():

    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class Stack():

    def __init__(self):
        self.len = 0
        self.head = None
        self.tail = None

    def push(self, data):
        """ Adds a Node to the top of the stack"""
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
            self.len += 1
        else:
            self.tail.next = Node(data)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
            self.len += 1

    def pop(self):
        """ Remove a node from the top of the stack"""
        temp = self.tail.prev
        self.tail.prev = None
        self.tail = temp
        self.tail.next = None
        self.len -= 1

    def print(self):
        traverse_point = self.tail
        while traverse_point.prev :
            print(str(traverse_point.data))
            traverse_point = traverse_point.prev
        print(str(traverse_point.data))

""" Example of a Stack """


stack = Stack()                 # Creating an empty stack

for i in range(10):             # Pushing to a stack the numbers 0-9
    stack.push(i)

stack.print()                   # Printing the stack to the screen
print('\n\n\n')

for i in range(2):              # Poping the 2 most recent items to the stack
    stack.pop()

stack.print()
print('\n\n\n')
                                # printing the number of items in the stack
print('There are ' + str(stack.len) + ' items in this stack')
