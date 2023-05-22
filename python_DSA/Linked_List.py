class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)

        else:
            last_node = self.head

            while last_node.next is not None:
                last_node = last_node.next

            last_node.next = Node(data, None)

    # Insertion at Value
    def insert_at_value(self, data, index):
        index = index-1
        item = self.head
        count = 1

        while item.next is not None:
            if count == index:
                item.next = Node(data, item.next)
                return
            else:
                item = item.next
                count += 1

    def delete_at_start(self):
        if self.head is None:
            print("List is Empty")
        else:
            self.head = self.head.next

    def delete_at_end(self):
        if self.head is None:
            print("List is Empty")
        else:
            item = self.head
            length = 1

            while item.next is not None:
                item = item.next
                length += 1

            index = length-1
            count = 1
            item1 = self.head

            while item1.next is not None:
                if count == index:
                    item1.next = None
                    break
                else:
                    item1 = item1.next
                    count += 1

    def delete_by_value(self, value):
        item = self.head
        count = 1
        index = 0

        while item.next is not None:
            if item.data == value:
                index = item.next
                break
            else:
                item = item.next
                count += 1

        ck_point = count - 1
        item1 = self.head
        count1 = 1

        while item1.next is not None:
            if count1 == ck_point:
                item1.next = index
                break
            else:
                item1 = item1.next
                count1 += 1

    def create_new_list(self, new_list1):
        self.head = None

        for data in new_list1:
            self.insert_at_end(data)

    def display(self):
        if self.head is None:
            print("List is Empty")
            return

        item = self.head

        while item is not None:
            print(item.data, end='-->')
            item = item.next


if __name__ == "__main__":

    ll = LinkedList()

    ll.insert_at_start(10)
    ll.insert_at_start(20)
    ll.insert_at_start(30)
    ll.insert_at_start(40)

    ll.insert_at_end(15)
    ll.insert_at_end(25)

    ll.insert_at_value(23, 3)
    ll.insert_at_value(12, 5)

    # ll.delete_at_start()

    # ll.delete_at_end()
    # ll.delete_at_end()

    # ll.delete_by_value(23)

    ll.display()
    print('\n')

    new_list1 = ['Mango', 'Apple', 'Banana', 'Grapes', 'Pineapple', 'Watermelon']
    ll.create_new_list(new_list1)

    ll.display()
