""" Linked List Data Structure in Python """

class Node():

    def __init__(self,data,next = ""):
        self.data = data
        self.next = next


class LinkedList():

    def __init__(self):
        self.len = 0
        self.head = -1
        self.tail = -1


    def append(self, data, next = None):
        if self.head == -1:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next



""" Example """
linked_list = LinkedList()

for i in range(10):
    linked_list.append(i)


data = True
traverse_point = linked_list.head
while data != False:
    print(str(traverse_point.data))
    traverse_point = traverse_point.next
