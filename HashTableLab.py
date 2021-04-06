#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      denad
#
# Created:     22/05/2020
# Copyright:   (c) denad 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

'''
contact={"Dejv":123456,'Alex':654987,'Mery':85647}

contactList=[("Dejv",123456),('Alex',654987),('Mery',85647)]

def addNew(data,key,value):
    data.append((key,value))

addNew(contactList,'Sara',12255)
print(contactList)

def findIt(data,key):
    for item in data:
        if item[0]==key:
            return item[1]

print(findIt(contactList,'Alex'))
'''

'''
hashTable=[None]*10

def hashFuncKey(data,key):
    return key% len(data)

def insert(data,key,value):
    hashKey=hashFuncKey(data,key)
    hashTable[hashKey]=value

insert(hashTable,10,'Alex')
print(hashTable)

insert(hashTable,14,'Mary')
print(hashTable)

insert(hashTable,14,'Deni')
print(hashTable)
'''

'''
hashTable=[[] for i in range(10)]
print(hashTable)

def hashFuncKey(data,key):
    return key%len(data)

def insert(data,key,value):
    hashkey=hashFuncKey(data,key)
    hashTable[hashkey]=hashTable.append((key,value))
'''

hashTable=[[] for i in range(10)]
print(hashTable)

def insert(data,key,value):
    hashKey = hash(key)%len(data)
    keyExist = False
    bucket = hashTable[hashKey]

    for i,kv in enumerate(bucket):
        k,v=kv
        if key==k:
            keyExist=True
            break;

    if keyExist:
        bucket[i]=((key,value))
    else:
        bucket.append((key,value))

insert(hashTable,10,'Alex')
print(hashTable)

insert(hashTable,14,'Mary')
print(hashTable)

insert(hashTable,20,'Martin')
print(hashTable)

insert(hashTable,10,'Deni')
print(hashTable)

def search(data,key):
    hashKey=hash(key)%len(data)
    bucket=data[hashKey]

    for kv in bucket:
        k,v=kv
        if key==k:
            return v

print(search(hashTable,10))

def delete(data,key):
    hashKey=hash(key)%len(data)
    keyExist=False
    bucket=data[hashKey]
    for i,kv in enumerate(bucket):
        k,v=kv
        if key==k:
            keyExist=True
            break;
    if keyExist:
        del bucket[i]
        print("Key {} deleted ".format(key))
    else:
        print("Key {} not found ".format(key))

delete(hashTable,10)
print(search(hashTable,10))
delete(hashTable,10)

insert(hashTable,140,'Deni')
print(hashTable)

insert(hashTable,140,'Denis')
print(hashTable)

insert(hashTable,120,'Martin')
print(hashTable)

insert(hashTable,130,'Fatos')
print(hashTable)