#-------------------------------------------------------------------------------
# Name:        quickSort.py
# Purpose:     Implementing the quickSort algorithm for different values of pivot.
#
# Author:      Denado Rabeli
#
# Created:     12/06/2020
# Copyright:   (c) denad 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random
import time
#To create a random array
def createRandArray(n):
    A=[random.randint(0,100) for i in range(n)]
    return A
#defining the partition starting from the left most number
def partitionL(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and array[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and array[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    array[start], array[high] = array[high], array[start]

    return high

def quick_sortL(array, start, end):
    if start >= end:
        return
    #call partition for the entire array
    p = partitionL(array, start, end)
    #after finding partition , run quickSort again for the part left of partition
    #and for the part on the right of partition
    quick_sortL(array, start, p-1)
    quick_sortL(array, p+1, end)

a=createRandArray(100)
#To get the running time we substract start from end (we also substract 1 because of sleep function.)
start=time.time()
quick_sortL(a,0,len(a)-1)
time.sleep(1)
end=time.time()
print("After left most pivot Sort:")
print("The running time was : {:f}".format(end-start-1))


def partitionR(array, start, end):
    #First we get a random position for pivot then replace it
    #at the beggining and call partition left
    randpivot = random.randint(start,end)

    array[start],array[randpivot]=array[randpivot],array[start]

    return partitionL(array,start,end)

def quick_sortR(array, start, end):
    if start >= end:
        return

    p = partitionR(array, start, end)
    quick_sortR(array, start, p-1)
    quick_sortR(array, p+1, end)

a=createRandArray(100)
start=time.time()
quick_sortR(a,0,len(a)-1)
time.sleep(1)
end=time.time()
print("After random pivot Sort:")
print("The running time was : {:f}".format(end-start-1))

def partitionM(array, start, end):
    #We get the middle position and replace it with the first one , then run
    #partitioning.
    midpivot = (start+end)//2

    array[start],array[midpivot]=array[midpivot],array[start]

    return partitionL(array,start,end)

def quick_sortM(array, start, end):
    if start >= end:
        return

    p = partitionM(array, start, end)
    quick_sortM(array, start, p-1)
    quick_sortM(array, p+1, end)

a=createRandArray(100)
start=time.time()
quick_sortM(a,0,len(a)-1)
time.sleep(1)
end=time.time()
print("After middle pivot Sort:")
print("The running time was : {:f}".format(end-start-1))

'''
For input of size 100 :
    The running time for left most was : 0.009998
    The running time for random was : 0.009999
    The running time for middle was : 0.006826

For input of size 1000:
    The running time for left most was : 0.010000
    The running time for random was : 0.000139
    The running time for middle was : 0.000109

For input of size 10000:
    The running time for left most was : 0.080212
    The running time for random was : 0.119965
    The running time for middle was : 0.080191

For input of size 100000:
    The running time for left most was : 1.306391
    The running time for random was : 1.372120
    The running time for middle was : 1.288913

For further bigger inputs the maximum recursion depth was exceeded .
As far as comparison is concerned we can see that the left most one was the most
stable one with the time going up the bigger the input .
The random one was the most unstable with the running time going up and down in
an unpredictable manner.
The middle pivot was the most efficient choice for this algorithm,
although a little unpredictable at times too.

'''