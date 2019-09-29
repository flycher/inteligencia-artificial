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
        """
        :attrib head: The head of the queue
        """
        self.head = QNode()
        self.tail = QNode()
        self.head.next = self.tail

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

    def get(self):
        """
        The get operation for the queue, removing the first node added
        :return: Returns the first node of the queue
        """
        try:
            node = self.head.next.value
            self.head = self.head.next
            return node
        except AttributeError:
            return None

    def peek(self):
        """
        Checks the first element of the queue
        :return: Returns the head of the queue
        """
        return self.head.next.value
