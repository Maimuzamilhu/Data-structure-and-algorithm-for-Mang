class Node:
    def __init__(self, data):
        self.data = data
        self.nextPtr = None


class LinkedList:
    def __init__(self):
        self.head = None

    ## insert the new node at the end of the linked list
    def insertAtEnd(self, new_data):
        ## create a new node for the new data
        new_node = Node(new_data)

        ## check whether linked list is empty or different
        if self.head is None:
            self.head = new_node
            return

        ## insert the data at the end
        temp = self.head
        while temp.nextPtr:
            temp = temp.nextPtr

        temp.nextPtr = new_node

    ## search for a given node inside the Linked List
    ## if node is present return True otherwise return False
    def searchNode(self, nodeData):
        ## write your code here
        temp = self.head
        while temp:
            if temp.data == nodeData:
                return True
            temp = temp.nextPtr

        return False

    ## print the linked list
    def printLinkedList(self):
        temp = self.head
        while temp:
            print(str(temp.data) + " ", end=" ")
            temp = temp.nextPtr


## Driver code
llist = LinkedList()

llist.insertAtEnd(10)
llist.insertAtEnd(20)
llist.insertAtEnd(30)
llist.insertAtEnd(40)
llist.insertAtEnd(50)
print("Insertion of nodes at the end of the Linked List:")
llist.printLinkedList()
print()

nodeData = 80
if llist.searchNode(nodeData):
    print("Data is present inside the Linked List")
else:
    print("No Data present inside the Linked List")
