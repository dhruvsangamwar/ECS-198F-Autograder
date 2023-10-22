class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def create_cycle(self, position):
        # Create a cycle by linking the last node to a node at the specified position
        if position < 0:
            return  # Invalid position
        current = self.head
        tail = None
        index = 0
        while current:
            if index == position:
                tail = current
            if not current.next:
                current.next = tail  # Create the cycle here
                return
            current = current.next
            index += 1

def has_cycle(linked_list):
    # Floyd's Cycle Detection Algorithm
    slow = linked_list.head
    fast = linked_list.head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True  # Cycle detected

    return False