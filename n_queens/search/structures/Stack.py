class QStack:
    """
    A class representing the node for a stack
    """

    def __init__(self):
        """
        :attrib value: The value associated with the node
        :attib prev: The previous node it points to
        """
        self.value = None
        self.prev = None


class Stack:
    """
    A class representing a stack implemented using linked list
    """

    def __init__(self):
        self.head = QStack()

    def push(self, node):
        """
        The push operation for the stack, adding to the end of the list
        :param node: The node to be added to the stack
        """
        new = QStack()
        new.value = node
        new.prev = self.head
        self.head = new

    def pop(self):
        """
        The pop operation for the stack, removing the last node added
        :return: Returns the last node of the queue
        """
        try:
            node = self.head.value
            self.head = self.head.prev
            return node
        except AttributeError:
            return None

    def peek(self):
        """
        Checks the first element of the stack
        :return: Returns the head of the stack
        """
        return self.head.value
