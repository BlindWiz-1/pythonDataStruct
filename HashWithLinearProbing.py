#-------------------------------------------------------------------------------
# Name:        HashWithLinearProbing.py
# Purpose:     To implement the hash that deals with collisions using linear probing
#
# Author:      Denado Rabeli
#
# Created:     22/05/2020
# Copyright:   (c) denad 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

hashTable = [(None, None) for i in range(10)]

def hashFuncKey(data,key):
    return key % len(data)

def insert(data, key, value):
    hashKey=hashFuncKey(hashTable,key)
    keyExists=False
    #To check if such a key already exists
    for i,kv in enumerate(hashTable):
        k,v=kv
        if key==k:
            keyExists=True
            break;
    #If key exists we replace it with new value
    if keyExists:
        hashTable[hashKey]=(key,value)
    #If key does't exist we first check if this position is free
    #Then if not we iterate through slots circularly until we find an empty one.
    else:
        if hashTable[hashKey]==(None,None):
            hashTable[hashKey]=(key,value)
        else:
            hashTable[findEmpty(hashTable,hashKey)]=(key,value)

def findEmpty(data,hashKey): #A function that will return an empty position after checking circularly.
    j=0
    for i in enumerate(hashTable):
        j+=1
        if hashTable[hashKey+j]==(None,None):
            return hashKey+j

def search(data,key):#Returns value if key of such value is found .
    keyExists=False
    for i,kv in enumerate(hashTable):
        k,v=kv
        if key==k:
            print(v)

def delete(data,key):#Function to replace a key-value pair with two deleted strings as shown in lab's output.

    hashKey=hashFuncKey(hashTable,key)
    keyExists=False
    for i,kv in enumerate(hashTable):
        k,v=kv
        if key==k:
            keyExists=True
            break;
    if keyExists:
        hashTable[hashKey]=('deleted','deleted')
    else:
        print("Not found !!")

'''
Running codes specified in the laboratory and checking their output if it's correct.
'''
insert(hashTable, 10, 'Alex')
insert(hashTable, 14, 'Mary')
insert(hashTable, 18, 'Deni')
insert(hashTable, 20, 'Jane')
insert(hashTable, 21, 'Besmir')
insert(hashTable, 30, 'Kejd')
insert(hashTable, 24, 'Rei')
insert(hashTable, 18, 'Rei')
print(hashTable)
'''
[(10, 'Alex'), (20, 'Jane'), (21, 'Besmir'), (30, 'Kejd'), (14, 'Mary'), (24, 'Rei'), (None,
None), (None, None), (18, 'Rei'), (None, None)]
'''
delete(hashTable, 10)
print(hashTable)
'''
[('deleted', 'deleted'), (20, 'Jane'), (None, None), (None, None), (14, 'Mary'), (None, None),
(None, None), (None, None), (18, 'Deni'), (None, None)]
'''
search(hashTable, 20)
'''
‘Jane’
'''
insert(hashTable, 10, 'Martin')
'''
[(10, 'Martin'), (20, 'Jane'), (21, 'Besmir'), (30, 'Kejd'), (14, 'Mary'), (24, 'Rei'), (None,
None), (None, None), (18, 'Rei'), (None, None)]
'''
search(hashTable, 20)
'''
‘Jane’
'''