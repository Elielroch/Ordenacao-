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
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def selection_sort(self):
        current = self.head
        while current:
            min_node = current
            runner = current.next
            while runner:
                if runner.data < min_node.data:
                    min_node = runner
                runner = runner.next

            current.data, min_node.data = min_node.data, current.data
            current = current.next


