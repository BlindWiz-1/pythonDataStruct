#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Denado Rabeli
#
# Created:     08/05/2020
# Copyright:   (c) denad 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
class BST:

    #This is the initializiaton of each BST object .
    def __init__(self,value):
        self.value=value
        self.left_child=None
        self.right_child=None

    #Insertion function which insert new nodes depending on their value .
    def insert_node(self,value):

        if self.value>=value and self.left_child: # if left exists recall function
            self.left_child.insert_node(value)

        elif self.value>=value: # if left doesn't exist enter it directly
            self.left_child=BST(value)

        elif self.value<value and self.right_child: #same as above
            self.right_child.insert_node(value)

        else:
            self.right_child=BST(value)#same as if there is no left

    #Print them in preorder traversal .
    def preOrder(self):
        print(self.value, end=' ')

        if self.left_child:
            self.left_child.preOrder()

        if self.right_child:
            self.right_child.preOrder()

    #prints them in postOrder traversal .
    def postOrder(self):

        if self.left_child:
            self.left_child.postOrder()

        if self.right_child:
            self.right_child.postOrder()

        print(self.value, end=' ')

    #Print the value of the smallest node .
    def findMin(self):
        #Go left to search for minimum
        if self.left_child!=None:

            return self.left_child.findMin()

        else:

            print(self.value)

    #Print value of the biggest node .
    def findMax(self):
        #Go right to check for maximum
        if self.right_child!=None:

            return self.right_child.findMax()

        else:

            print(self.value)

    #Find if the node searched by user is present or not and return 1 if yes and
    #0 otherwise .
    def findNode(self,data):
        #if value found return 1
        if self.value==data:
            return 1
        #if smaller go left , also checking if next child is empty
        elif self.left_child and self.value>data:
            return self.left_child.findNode(data)
        #if it is bigger than self value go right , same as above
        elif self.right_child and self.value<data:
            return self.right_child.findNode(data)
        #if not found return 0
        else:
            return 0


#Entering input and dividing it .
n=input()
a=list(map(int,n.split()))

#setting the root so that the insertion function can work .
b=BST(a[0])

#To insert each node value .
for i in range(1,len(a)):
    b.insert_node(a[i])

#To print them in pre-order traversal .
print("PRE - ORDER")
b.preOrder()

#To print them in post-order traversal .
print()
print("POST-ORDER")
b.postOrder()

#Printing the max and min of our functions .
print()
print("Min is :")
b.findMin()
print("Max is :")
b.findMax()

#Checking for a certain value if found or not
print("Was it found YES/1 NO/0 ?")
print(b.findNode(50))
