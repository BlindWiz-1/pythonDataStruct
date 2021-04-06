#-------------------------------------------------------------------------------
# Name:        mergeSort.py
# Purpose:     Implementing the merge sort algorithm .
#
# Author:      Denado Rabeli
#
# Created:     12/06/2020
# Copyright:   (c) denad 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random
import time

def createRandArray(n):
    A=[random.randint(0,100) for i in range(n)]
    return A

def mergeSort(array):
    if len(array)>1:
        #finding where middle is (using // to divide insures that we get an int)
        mid=len(array)//2
        #Dividing into two arrays using the found middle
        left=array[:mid]
        right=array[mid:]
        #Calling merge sort for the two arrays.
        mergeSort(left)
        mergeSort(right)

        i,j,k=0,0,0 #setting initial values at 0.

        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                array[k]=left[i]
                i+=1
            else:
                array[k]=right[j]
                j+=1
            k+=1
        #To make sure there are no elements left.
        while i<len(left):
            array[k]=left[i]
            i+=1
            k+=1

        while j<len(right):
            array[k]=right[j]
            j+=1
            k+=1

A=createRandArray(1000000)
start=time.time()#To calculate the running time of algorithm
mergeSort(A)
time.sleep(1)
end=time.time()
print("The running time was : {:f}".format(end-start-1))

'''
n=100 The running time was : 0.000748
n=1000 The running time was : 0.010264
n=10000 The running time was : 0.080218
n=100000 The running time was : 0.852124
n=1000000 The running time was : 9.672282

As we can see for smaller values of the input the running time of quick sort is
smaller, but for greater values the merge sort algorithm is faster and more efficient .
This is easily proven by the fact that for n=100000 at the quick sort algorithm we got
an error maximum depth of recursion reached .
'''
