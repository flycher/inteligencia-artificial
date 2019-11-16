class QNode:
    """
    A class representing a node for a queue
    """

    def __init__(self, value=None):
        self.value = value
        self.next = None


class Queue:
    """
    A class representing a queue implemented using linked list
    """

    def __init__(self):
        self.head = QNode()
        self.tail = QNode()
        self.head.next = self.tail
        self.length = 0

    def put(self, node):
        """
        The put operation for the queue, adding to the end of the linked list
        :param node: The node to be put in the queue
        """
        if self.tail.value is None:
            self.tail.value = node
        else:
            new = QNode(node)
            self.tail.next = new
            self.tail = new
        self.length += 1

    def get(self):
        """
        The get operation for the queue, removing the first node added
        :return: Returns the first node of the queue
        """
        try:
            node = self.head.next.value
            self.head = self.head.next
            self.length -= 1
            return node
        except AttributeError:
            return None

    def empty(self):
        """
        Checks the first element of the queue
        :return: Returns the head of the queue
        """
        return self.length == 0
