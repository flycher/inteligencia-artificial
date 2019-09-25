class QNode:
    """
    A class representing a node for a queue
    """

    def __init__(self):
        self.value = None
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

    def push(self, node):
        """
        The push operation for the queue, adding to the end of the list
        :param node: The node to be put in the queue
        """
        actual = self.head
        while actual.value is not None:
            actual = actual.next
        actual.value = node
        actual.next = QNode()

    def pop(self):
        """
        The pop operation for the queue, removing the first node added
        :return: Returns the first node of the queue
        """
        try:
            node = self.head.value
            self.head = self.head.next
            return node
        except AttributeError:
            return None

    def peek(self):
        """
        Checks the first element of the queue
        :return: Returns the head of the queue
        """
        return self.head.value
