_  #!/bin/python3

import math
import os
import random
import re
import sys


class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node


def print_doubly_linked_list(node, sep, fptr):
    while node:
        node = node.next


def sortedInsert(llist, data):
    new_node = DoublyLinkedListNode(data)
    temp = llist
    while temp is not None:
        if temp.data < data:
            if temp.prev is None:
                temp.prev = new_node
                new_node.next = temp
                llist.head = new_node
                return True
            else:
                new_node.next = temp
                new_node.prev = temp.prev
                temp.prev = new_node
                return True
        temp = temp.next
    return False

    # Write your code here


if __name__ == "__main__":

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)
