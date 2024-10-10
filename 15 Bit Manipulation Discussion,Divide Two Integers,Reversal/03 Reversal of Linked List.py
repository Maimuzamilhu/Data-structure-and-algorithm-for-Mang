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

    ## to reverse the singly linked list
    def reverseList(self):
        prev = None
        next = None
        curr = self.head

        while curr:
            next = curr.nextPtr
            curr.nextPtr = prev
            prev = curr
            curr = next

        ## update the head pointer
        self.head = prev

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
llist.insertAtEnd(150)
llist.insertAtEnd(250)
print("Insertion of nodes at the end of the Linked List:")
llist.printLinkedList()
print()

llist.reverseList()
print("Reversal of linked list:")
llist.printLinkedList()
print()