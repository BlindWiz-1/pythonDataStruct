#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      denad
#
# Created:     06/05/2020
# Copyright:   (c) denad 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class BinaryTree():

    def __init__(self,value):
        self.value=value
        self.right_child=None
        self.left_child=None

    def insertRight(self,value):

        if self.right_child==None:
            self.right_child=BinaryTree(value)
        else:
            new=BinaryTree(value)
            new.right_child=self.right_child
            self.right_child=new

    def insertLeft(self,value):

        if self.left_child==None:
            self.left_child=BinaryTree(value)
        else:
            new= BinaryTree(value)
            new.left_child=self.left_child
            self.left_child=new

    def preOrder(self):

        print(self.value)
        if self.left_child:
            self.left_child.preOrder()
        if self.right_child:
            self.right_child.preOrder()

    def postOrder(self):

        if self.left_child:
            self.left_child.postOrder()
        if self.right_child:
            self.right_child.postOrder()
        print(self.value)

n=BinaryTree('A')
n.insertLeft('B')
n.insertRight('C')

n1=n.left_child
n1.insertRight('X')

n.preOrder()
print("''''''''''''''''''''''")
n.postOrder()