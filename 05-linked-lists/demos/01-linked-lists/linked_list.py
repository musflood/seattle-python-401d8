from node import Node


class LinkedList:
    """Doc String"""
    def __init__(self, iter=[]):
        self._current = None
        self.head = None
        self._size = 0

        # l = LinkedList([1, 2, 3, 4])
        for item in reversed(iter):
            self.insert(item)
        # l.head => 1 -> 2 -> 3 -> 4 ->

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
