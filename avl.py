
class Node(object):

    def __init__(self,data):
        self.data = data
        self.height = 0
        self.leftChild = None
        self.rightChild = None

class AVL(object):

    def __init__(self):
        self.root = None

    def insert(self,data):
        self.root = self.insertNode(data,self.root)

    def insertNode(self,data,node):
        if not node:
            return Node(data)
        if data<node.data:
            node.leftChild = self.insertNode(data,node.leftChild)
        else:
            node.rightChild = self.insertNode(data,node.rightChild)

        node.height = max (self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1

        return self.settleViolation(data,node);

    def settleViolation(self,data,node):
        balance = self.calcBalance(node)

        # case 1: left left heavy situation; single right rotation
        if balance > 1 and data < node.leftChild.data:
            print("Left left heavy situation..")
            return self.rotateRight(node)

        # case 2: right right heavy situation; single left rotation
        if balance < -1 and data>node.rightChild.data:
            print("Right right heavy situation..")
            return self.rotateLeft(node)

        #case 3:
        if balance > 1 and data > node.leftChild.data:
            print("Left right heavy situation...")
            node.leftChild = self.rotateLeft(node.leftChild);
            return self.rotateRight(node)

        #case 4:
        if balance < -1 and data < node.rightChild.data:
            print("Right left heavy situation..")
            node.rightChild = self.rotateRight(node.rightChild);
            return self.rotateLeft(node)

        return node; 

    def calcHeight(self,node):

        if not node:
            return -1

        return node.height
    # if it returns value > 1 it means it is a left heavy tree --> right rotation
    # if it returns value < -1 it means it is right heavy tree --> left rotation

    def calcBalance(self,node):

        if not node:
            return 0;
        return (self.calcHeight(node.leftChild) - self.calcHeight(node.rightChild))

    #inorder traversal
    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)

    def traverseInOrder(self,node):

        if node.leftChild:
            self.traverseInOrder(node.leftChild)

        print("%s" % node.data)

        if node.rightChild:
            self.traverseInOrder(node.rightChild)
            
    def rotateRight(self,node):

        print("Roatating to the right on node ",node.data)

        tempLeftChild = node.leftChild
        t = tempLeftChild.rightChild

        tempLeftChild.rightChild = node
        node.leftChild = t

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1
        tempLeftChild.height = max(self.calcHeight(tempLeftChild.leftChild),self.calcHeight(tempLeftChild.rightChild)) + 1

        return tempLeftChild
    
    

    def rotateLeft(self,node):

        print("Roatating to the left on node ",node.data)

        tempRightChild = node.rightChild
        t = tempRightChild.leftChild

        tempRightChild.leftChild = node
        node.rightChild = t

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1
        tempRightChild.height = max(self.calcHeight(tempRightChild.leftChild),self.calcHeight(tempRightChild.rightChild)) + 1

        return tempRightChild

avl = AVL()
avl.insert(1)
avl.insert(2)
avl.insert(3)
avl.insert(4)
avl.insert(5)
avl.insert(6)
avl.traverse()
