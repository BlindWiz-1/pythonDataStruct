#-------------------------------------------------------------------------------
# Name:        singlyQueue.py
# Purpose:     Building a queue class using single linked list with all it's
#              functions
# Author:      Denado Rabeli
#
# Created:     27/04/2020
# Copyright:   (c) denad 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class singlyQueue:
    class Node:
        #Declaring how each node is constructed and making node a subclass of
        #queue.
        __slots__='element','next' #Using slot to use memory more efficiently
        def __init__(self,element,next):
            self.element=element
            self.next=next

    def __init__(self):
        #Creating a new empty stack
        self.head=None
        self.size=0

    def len(self):
        #Return size of list (Total number of nodes in it)
        return self.size

    def isEmpty(self):
        #Return True if it's empty.
        if(self.size==0):
            return True

    def push(self,e):
        #Adding new element in this queue
        #When we add in a queue we always add as a head
        new=self.Node(e,self.head)
        self.head=new
        self.size+=1

    def pop(self):
        #Used to pop out the head in accordance to LIFO(last in first out)logic
        if self.isEmpty():
             return 'Empty stack'
        answer=self.head.element
        self.head=self.head.next
        return answer


    def top(self):
        #When empty it will return a warning .
        if self.isEmpty():
            return 'Empty Stack'

        return self.head.element #return element of node in top of stack.

    def display(self):
        #We set as first node the head of list
        Node=self.head

        if self.isEmpty():
            return 'Empty'
        #Then we iterate until the Node is NONE.(end of list is reached)
        while(Node!=None):
            print(str(Node.element),end=' ')
            Node=Node.next
