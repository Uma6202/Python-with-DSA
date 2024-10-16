class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, value):
        if self.is_full():
            print("Queue is full!")
            return
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        removed_value = self.queue[self.front]
        if self.front == self.rear:  # Queue is now empty
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return removed_value

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        i = self.front
        while True:
            print(self.queue[i], end=' ')
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()
