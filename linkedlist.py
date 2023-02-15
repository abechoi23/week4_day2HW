class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_first(self, value):
        # create a new node with the given value
        new_node = Node(value)
        # set the new node's next to the current head
        new_node.next = self.head
        # update the head to be the new node
        self.head = new_node
        # increment the size of the linked list
        self.size += 1

    def add_last(self, value):
        # create a new node with the given value
        new_node = Node(value)
        # if the linked list is empty, set the head to the new node
        if not self.head:
            self.head = new_node
        else:
            # iterate through the linked list until the last node
            current = self.head
            while current.next:
                current = current.next
            # set the last node's next to the new node
            current.next = new_node
        # increment the size of the linked list
        self.size += 1

    def remove_first(self):
        if not self.head:
            # if the linked list is empty, return None
            return None
        else:
            # get the value of the current head
            value = self.head.value
            # set the head to the next node
            self.head = self.head.next
            # decrement the size of the linked list
            self.size -= 1
            # return the value of the removed node
            return value

    def remove_last(self):
        if not self.head:
            # if the linked list is empty, return None
            return None
        elif not self.head.next:
            # if the linked list has only one node, remove the head
            value = self.head.value
            self.head = None
            self.size -= 1
            return value
        else:
            # iterate through the linked list until the second to last node
            current = self.head
            while current.next.next:
                current = current.next
            # get the value of the last node
            value = current.next.value
            # remove the last node
            current.next = None
            # decrement the size of the linked list
            self.size -= 1
            # return the value of the removed node
            return value

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# create a new linked list
my_list = LinkedList()

# add some values to the linked list
my_list.add_first(1)
my_list.add_first(2)
my_list.add_last(3)

# remove the first value from the linked list
my_list.remove_first()

# remove the last value from the linked list
my_list.remove_last()

# print the size of the linked list
print(my_list.size)