#!/usr/bin/python3

'''A module for a singly linked list.

Classes:
    Node: A klas representing a node of a singly linked list
    LinkedList: the actual klas of the linked list
'''


class Node:
    '''A klas representing an instance of a linked list'''

    def __init__(self, data, next_node=None):
        '''instantiates an instance of a `Node` klas

        Args:
            data (int): the data to be stored in a node
            next_node (obj: `Node`, optional): a pointer to the next node
        '''
        self.data = data
        self.next_node = next_node

        @property
        def data(self):
            '''retrieves and sets the data private attribute of instances'''
            return self.__data

        @data.setter
        def data(self, value):
            if not isinstance(data, int):
                raise TypeError("data must be an integer")

            self.__data = value

        @property
        def next_node(self):
            '''A pointer to the next node in a host singly linked list'''
            return self.__next_node

        @next_node.setter
        def next_node(self, value):
            if value is not None and not isinstance(value, Node):
                raise TypeError("next_node must be a Node object")

            self.__next_node = value


class SinglyLinkedList:
    '''A singly linked list klas'''

    def __init__(self):
        '''initializes an instance of a singly linked list

        Attributes:
            __head (obj: Node, None): pointer to the head of the list
        '''
        self.__head = None

    def __str__(self) -> str:
        '''prints the linked list each node per line'''
        s = ''
        next = self.__head
        while next:
            s += str(next.data)
            if next.next_node:
                s += '\n'
            next = next.next_node
        return s

    def sorted_insert(self, value):
        '''inserts a node in a sorted manner'''
        value = Node(value)
        if not self.__head:
            self.__head = value
        else:
            if value.data < self.__head.data:
                self.__head, value.next_node = value, self.__head
                return

            curr = self.__head
            while curr:
                if curr.next_node is None:
                    curr.next_node = value
                    break
                if value.data < curr.next_node.data:
                    temp = curr.next_node
                    curr.next_node = value
                    value.next_node = temp
                    break

                curr = curr.next_node

        return
