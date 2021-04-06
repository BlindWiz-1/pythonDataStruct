#-------------------------------------------------------------------------------
# Name:        maxHeap.py
# Purpose:     Implementation of the max heap priority queue.
#
# Author:      Denado Rabeli
#
# Created:     15/05/2020
# Copyright:   (c) denad 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class maxHeapPriorityQueue:

    def __init__(self):
        self.queue=[]

    def parent(self,j): #Indice of it's parent

        return (j-1)//2 #Returning parent's position

    def rightChild(self,j): #returns indice of the right child

        return 2*j+2

    def leftChild(self,j):#returns indice of the left child

        return 2*j+1

    def hasLeft(self,j):#Checks if it has left child by checking if it's out of queue range

        return self.leftChild(j) < len(self.queue)

    def hasRight(self,j):#Checks if it has right child same as above

        return self.rightChild(j) < len(self.queue)

    def swap(self,i,j): #Swapping using a temporary variable

        temp=self.queue[i]
        self.queue[i]=self.queue[j]
        self.queue[j]=temp


    def upheap(self,j):

        parentPos=self.parent(j)

        if j>0:#To make sure we are not at the initial root.

            if (self.queue[j]>self.queue[parentPos]):

                self.swap(j,parentPos)#Swapping if condition is fulfilled.
                self.upheap(parentPos)#Recursion

    def downheap(self,j):

        if self.hasLeft(j): # Checking if it has left first,
                            #Because if it didn't have left it wouldn't have right either
            l=self.leftChild(j)
            small=l         #setting small to leftChild index

            if self.hasRight(j): #Checking for right
                if self.queue[self.rightChild(j)]>self.queue[l]:#Comparing right to left
                    small=self.rightChild(j)#if r is smaller set small index to rightChild
            if self.queue[small]>self.queue[j]:#Check value of parent to that of node at index small
                self.swap(j,small)
                self.downheap(small)

    def add(self,value):

        (self.queue).append(value)#Adding value at end of queue
        self.upheap(len(self.queue)-1)#Calling upheap to set it in the right location in min heap.


    def min(self):#Returns value of the smallest node

        return self.queue[0]

    def removeMax(self): #Removes the first node

        if self.nrOfNodes()==0:
            return "It's Empty ."

        last=len(self.queue)-1
        self.swap(0,last)
        removedMax=(self.queue).pop()
        self.downheap(0)
        return removedMax

    def nrOfNodes(self): #Nr of nodes in the heap
        return len(self.queue)

    def kSmallestElement(self,k):
        #Check condition if empty or if k is bigger than nr of nodes
        if self.nrOfNodes()==0:
            return "It's Empty ."
        if k>self.nrOfNodes():
            return "Enter another Number"
        #Sorting our nodes from smallest to biggest
        arr=sorted(self.queue)
        arr1=[]

        for i in range(k):
            arr1.append(arr[i]) # Setting first k smallest elements to array that is to be returned

        return arr1

    def kLargestElement(self,k):

        if self.nrOfNodes()==0:
            return "It's Empty ."
        if k>self.nrOfNodes():
            return "Enter another Number"

        arr=sorted(self.queue,reverse=True) #Sorting elements from biggest to smallest
        arr1=[]

        for i in range(k):
            arr1.append(arr[i])

        return arr1

'''
40 30 32 35 80 90 100 120 trial input
'''

'''
Calls for all the functions above to check if they are right or not .
'''
h=maxHeapPriorityQueue()

n=input()
a=list(map(int,n.split()))

h.add(a[0])

for i in range(1,len(a)):
    h.add(a[i])

print("maxHeap:",h.queue)

print(h.kSmallestElement(4))

print(h.kLargestElement(4))

for i in range (h.nrOfNodes()):
    print(h.removeMax(),end=' ')

'''
Output:

40 30 32 35 80 90 100 120
maxHeap: [120, 100, 90, 40, 35, 32, 80, 30]
[30, 32, 35, 40]
[120, 100, 90, 80]
120 100 90 80 40 35 32 30

'''











