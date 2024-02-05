# def insert_after_value(self, data_after, data_to_insert):
#     # Search for first occurrence of data_after value in linked list
#     # Now insert data_to_insert after data_after node
#
# def remove_by_value(self, data):
#     # Remove first node that contains data

# ll = LinkedList()
# ll.insert_values(["banana", "mango", "grapes", "orange"])
# ll.print()
# ll.insert_after_value("mango", "apple")  # insert apple after mango
# ll.print()
# ll.remove_by_value("orange")  # remove orange from linked list
# ll.print()
# ll.remove_by_value("figs")
# ll.print()
# ll.remove_by_value("banana")
# ll.remove_by_value("mango")
# ll.remove_by_value("apple")
# ll.remove_by_value("grapes")
# ll.print()


class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            return self.insert_at_beginning(data)

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next

        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            if count == index - 1:
                itr.next = itr.next.next
                break
            count += 1

    def print(self):
        if self.head is None:
            print("Linked List is Empty")
            return

        itr = self.head
        linked_list_string = ""
        while itr:
            suffix = ""
            if itr.next:
                suffix = "----->"
            linked_list_string += str(itr.data) + suffix  # Append data in linked_list_string
            itr = itr.next
        print(linked_list_string)

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return

        count = 0
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
            itr = itr.next
            count += 1

    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        count = 0
        while self.head:
            if self.head.data == data:
                self.head.next = self.head.next.next
                break
            self.head = self.head.next
            count += 1


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_values(["banana", "mango", "grapes", "orange"])
    linked_list.print()
    linked_list.insert_after_value("mango", "apple")
    linked_list.print()
    linked_list.remove_by_value("orange")
    linked_list.print()
    linked_list.remove_by_value("figs")
    linked_list.print()
    linked_list.remove_by_value("banana")
    linked_list.remove_by_value("mango")
    linked_list.remove_by_value("apple")
    linked_list.remove_by_value("grapes")
    linked_list.print()
