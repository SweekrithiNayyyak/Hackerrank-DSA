#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
# Complete the printLinkedList function below.

class SinglyLinkedList:
    def __init__(self):
        new_node=Node(None)
        self.head=new_node
        self.tail=new_node
        self.length=0
    def insert_node(self,value):
        new_node=Node(value)
        if self.head.value is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
        # print(self.head.value)
            
            
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
# #
def printLinkedList(head):
    temp=head
    while temp:
        print(temp.value)
        
        temp=temp.next
        
        

if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    printLinkedList(llist.head)
