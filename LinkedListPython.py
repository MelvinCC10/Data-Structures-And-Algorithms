""" Linked List Data Structure in Python """

class Node():

    def __init__(self,data,next = ""):
        self.data = data
        self.next = next


""" Example """

node1 = Node("5")
node2 = Node("7")
node3 = Node("4")
node4 = Node("2")

node1.next = node2
node2.next = node3
node3.next = node4

next = True
currentnode = node1

while next:
    print(currentnode.data)
    currentnode = currentnode.next
