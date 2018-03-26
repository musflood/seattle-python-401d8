from linked_list.node import Node


class LinkedList:
    """Doc String"""
    def __init__(self, iter=[]):
        # Scott defined this for something we will cover later
        # self._current = None
        self.head = None
        self._size = 0

        # l = LinkedList([1, 2, 3, 4])
        try:
            for item in reversed(iter):
                self.insert(item)
            # l.head => 1 -> 2 -> 3 -> 4 ->
        except TypeError:
            print('Please pass an iterable.')

    def __repr__(self):
        # Assuming head will have a val (You need to handle the case of None)
        return '<head> => {}'.format(self.head.val)

    def __len__(self):
        return self._size

    def insert(self, val):
        # node = Node(val)
        # node.next = self.head
        # self.head = node

        self.head = Node(val, self.head)
        self._size += 1

    def find(self, val):
        # create a pointer for current => self.head
        # do a while loop
        # while current is not none

        current = self.head

        while current:
            if val == current.val:
                return True

            current = current._next

        return False
