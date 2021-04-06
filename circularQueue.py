#-------------------------------------------------------------------------------
# Name:        circularQueue.py
# Purpose:     To write the Queue class using circular linked list.
#
# Author:      Denado Rabeli
#
# Created:     27/04/2020
# Copyright:   (c) denad 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class circularQueue:

    class Node:

        __slot__='element','next'

        def __init__(self,element,next):
            self.element=element
            self.next=next

    def __init__(self):
        self.current=None
        self.size=0

    def len(self):
        #Return size of list(Total number of nodes in it)
        return self.size

    def isEmpty(self):
        #Return True if it's empty.
        if(self.size==0):
            return True

    def enqueue(self,e):#Insert directly after current
        new=self.Node(e,None)
        if self.size==0:

            new.next=new

        else:

            new.next=self.current.next
            self.current.next=new #the first and last one will keep pointing to
                                  #each other

        self.current=new #New added node is set as current
        self.size+=1

    def dequeue(self):
        if self.isEmpty(): #Check if empty
            return "It's Empty "
        old=self.current.next
        if self.size==1: #Removing only element
            self.current=None   #Queue is empty
        else:
            self.current.next=old.next
        self.size-=1
        return old.element

    def display(self):  #Displaying elements of the queue
        if self.isEmpty():
            return "It's empty"
        else :
            node=self.current
            for i in range (self.len()):
                print(node.element)
                node=node.next




