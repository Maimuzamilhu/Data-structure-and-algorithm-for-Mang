
class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, data):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full.")
            return
        elif self.front == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty.")
            return
        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.front = self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp

    def peek(self):
        if self.front == -1:
            print("Queue is empty.")
            return
        return self.queue[self.front]

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def display(self):
        if self.front == -1:
            print("Queue is empty.")
            return
        if self.rear >= self.front:
            print(self.queue[self.front:self.rear+1])
        else:
            print(self.queue[self.front:] + self.queue[:self.rear+1])

# Example usage
q = Queue(5)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()  # Output: [1, 2, 3]
q.dequeue()
q.display()  # Output: [2, 3]
