class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Creation of linked list
    def create(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Insertion at the end
    def insert(self, data):
        self.create(data)

    # Deletion of a node by value
    def delete(self, key):
        current = self.head
        previous = None

        while current and current.data != key:
            previous = current
            current = current.next

        if current is None:  # Key not found
            print("Value not found in the list.")
            return

        if previous is None:  # The node to be deleted is the head
            self.head = current.next
        else:
            previous.next = current.next

    # Display the linked list
    def display(self):
        current = self.head
        if current is None:
            print("The list is empty.")
            return
        
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    
    # Creation of linked list
    ll.create(1)
    ll.create(2)
    ll.create(3)

    print("Initial Linked List:")
    ll.display()

    # Insertion of new element
    ll.insert(4)
    print("After inserting 4:")
    ll.display()

    # Deletion of an element
    ll.delete(2)
    print("After deleting 2:")
    ll.display()

    # Attempt to delete a non-existent element
    ll.delete(5)
