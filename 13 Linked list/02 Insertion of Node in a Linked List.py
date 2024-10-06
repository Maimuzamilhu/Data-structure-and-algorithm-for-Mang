class Node:
    def __init__(self, data):
        self.data = data
        self.nextPtr = None


class LinkedList:
    def __init__(self):
        self.head = None

    '''
    ## insert the new node at the beginning of the linked list
    def insertAtbeginning(self, new_data):
      ## create a new node for the new_data
      new_node = Node(new_data)
      ## insertion at the beginning of the linked list
      new_node.nextPtr = self.head
      self.head = new_node
    '''

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

    ## insert the new node after any of the previous node
    def insertAfterNode(self, prev_node, new_data):
        if prev_node is None:
            print("Given node must be available in your linked list")
            return

        ##create a new linked list
        new_node = Node(new_data)
        new_node.nextPtr = prev_node.nextPtr
        prev_node.nextPtr = new_node

    ## print the linked list
    def printLinkedList(self):
        temp = self.head
        while temp:
            print(str(temp.data) + " ", end=" ")
            temp = temp.nextPtr


## Driver code
llist = LinkedList()
'''
llist.insertAtbeginning(10)
llist.insertAtbeginning(20)
llist.insertAtbeginning(30)
llist.insertAtbeginning(40)
llist.insertAtbeginning(50)
llist.printLinkedList()
'''

llist.insertAtEnd(10)
llist.insertAtEnd(20)
llist.insertAtEnd(30)
llist.insertAtEnd(40)
llist.insertAtEnd(50)
print("Insertion of nodes at the end of the Linked List:")
llist.printLinkedList()
print()
llist.insertAfterNode(llist.head.nextPtr, 25)
print("Insertion of nodes after second node of the linked list:")
llist.printLinkedList()