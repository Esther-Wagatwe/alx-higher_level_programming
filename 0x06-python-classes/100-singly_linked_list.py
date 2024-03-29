#!/usr/bin/python3

"""Define classes for a singly-linked list."""


class Node:
    """
    Class that defines properties Node.

    Attributes:
        data: data field of node.
    """
    def __init__(self, data, next_node=None):
        """Initialize a new Node.

        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the data of the Node."""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/set the next_node of the Node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Class that defines properties of SinglyLinkedList.

    Attributes:
       head: head of the SinglyLinkedList.
    """
    def __init__(self):
        """Initalize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.

        The node is inserted into the linked list at the correct
        ordered numerical position.

        Args:
            value (Node): The new Node to insert.
        """
        new_node = Node(value)

        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while (current.next_node and current.next_node.data < value):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        result = []
        current = self.__head
        while current is not None:
            result.sort()
            result.append(str(current.data))
            current = current.next_node
        result.sort(key=int)
        return ('\n'.join(result))
