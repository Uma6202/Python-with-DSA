class Node:
    """A node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    """A singly linked list."""
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Insert a new node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Insert a new node at the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete_node(self, key):
        """Delete the first occurrence of a node with the given key."""
        current = self.head

        # If the node to be deleted is the head node
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        # Search for the key to be deleted
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If the key was not found
        if not current:
            print("Node with data", key, "not found.")
            return

        # Unlink the node
        prev.next = current.next
        current = None

    def search(self, key):
        """Search for a node with the given key."""
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def display(self):
        """Display the linked list."""
        current = self.head
        if not current:
            print("List is empty.")
            return
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("None")

# Example usage
if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    linked_list.insert_at_end(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_beginning(5)
    linked_list.display()  # Output: 5 -> 10 -> 20 -> None

    linked_list.delete_node(10)
    linked_list.display()  # Output: 5 -> 20 -> None

    found = linked_list.search(20)
    print("Node found:", found)  # Output: Node found: True

    linked_list.display()  # Output: 5 -> 20 -> None
