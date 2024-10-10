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

    ## to detect the loop inside the linked list
    def detectLoop(self):
        hare = self.head
        tortoise = self.head

        while tortoise and hare and hare.nextPtr:
            hare = hare.nextPtr.nextPtr #two step
            tortoise = tortoise.nextPtr #one step

            if tortoise == hare:
                return True
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

## make a loop inside the linked list
llist.head.nextPtr.nextPtr.nextPtr = llist.head

if llist.detectLoop():
    print("Loop is inside the Linked List")
else:
    print("No Loop")