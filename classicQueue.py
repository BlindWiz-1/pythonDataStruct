#-------------------------------------------------------------------------------
# Name:        classicQueue.py
# Purpose:     Building a queue using array circularly
#
# Author:      Denado Rabeli
#
# Created:     27/04/2020
# Copyright:   (c) denad 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class classicQueue:
    #default size of 10
    default=10

    #constructor of this class
    def __init__(self):
        self.data=[None]*classicQueue.default
        self.size=0
        self.front=0

    def __len__(self):#Returns length
        return self.size == 0

    def isEmpty(self):#For empty queue returns true
        if self.size==0:
            return True

    def first(self):#Returns the front element
        if self.isEmpty():
            return 'Empty'
        return self.data[self.front]

    #to remove element from the bottom of queue. FIFO
    def dequeue(self):

        if self.isEmpty():
            return 'Nothing to dequeue'

        ans=self.data[self.front]
        self.data[self.front]=None
        self.front=(self.front+1)%len(self.data)
        self.size-=1
        return ans

    def resize(self,cap):

        old=self.data
        #Creating a new array with bigger size in values will be stored
        self.data=[None]*cap
        walk=self.front
        #To copy the old one .
        for k in range(self.size):
            self.data[k]=old[walk]
            walk=(1+walk)%len(old)

    #To add new element in top
    def enqueue(self,e):

        if self.size==len(self.data):
            self.resize(2*len(self.data))

        rear=(self.front+self.size)%len(self.data)
        self.data[rear]=e
        self.size+=1

    #To display elements
    def display():
        for i in range(len(self.data)):
            print(self.data[i])

