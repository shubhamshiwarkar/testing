class Node:
    def __init__(self, data=None):
        self.prev = None
        self.data = data
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            item = self.head

            while item.next is not None:
                item = item.next

            item.next = node
            node.prev = item

    def insert_before_node(self, data, node_value):
        node = Node(data)
        item = self.head
        count = 1

        while item is not None:
            if item.data == node_value:
                item.prev = node
                node.next = item
                break
            else:
                item = item.next
                count += 1

        count = count - 1
        count1 = 1
        item1 = self.head

        while item1 is not None:
            if count1 == count:
                item1.next = node
                node.prev = item1
                break
            else:
                item1 = item1.next
                count1 += 1

    def insert_after_node(self, data, node_value):
        node = Node(data)
        item = self.head
        count = 1

        while item is not None:
            if item.data == node_value:
                item.next = node
                node.prev = item
                break
            else:
                item = item.next
                count += 1

        count = count + 1
        count1 = 1
        item1 = self.head

        while item1 is not None:
            if count1 == count:
                item1.prev = node
                node.next = item1
                break
            else:
                item1 = item1.next
                count1 += 1

    def display_forward(self):
        if self.head is None:
            print("List is Empty")
        else:
            item = self.head

            while item is not None:
                print(item.data, end="<==>")
                item = item.next

    def display_backward(self):
        if self.head is None:
            print("List is Empty")
        else:
            item = self.head

            while item.next is not None:
                item = item.next

            while item is not None:
                print(item.data, end="<==>")
                item = item.prev


if __name__ == "__main__":

    dll = DoublyLinkedList()

    dll.insert_at_start(10)
    dll.insert_at_start(20)
    dll.insert_at_start(30)
    dll.insert_at_start(40)

    dll.insert_at_end(15)
    dll.insert_at_end(25)

    dll.insert_before_node(32, 20)

    dll.insert_after_node(34, 30)

    dll.display_forward()
    print("\n")
    dll.display_backward()
