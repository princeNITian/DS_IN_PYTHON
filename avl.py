class Node:
    def __init__(self,data):
        self.data = data
        self.height = 0
        self.leftChild = None
        self.rightChild = None
        
#create AVL class 
class AVL:
    def __init__(self):
        self.root = None
        
    def calcHeight(self,node):
        if not node:
            return -1
        return node.height
        
    def calcBalance(self,node):
        if not node:
            return 0
        return (self.calcHeight(node.leftChild)-self.calcHeight(node.rightChild))
        
    #rotate right
    def rotateRight(self,node):
        print("Rotating to the right on node",node.data)
        tempLeftNode = node.leftChild
        t = tempLeftNode.rightChild
        tempLeftNode.rightChild = node
        node.leftChild = t
        #update height
        node.height = max(self.calcHeight(node.leftChild),self.calcHeight(node.rightChild)) + 1
        tempLeftNode.height = max(self.calcHeight(tempLeftNode.leftChild),self.calcHeight(tempLeftNode.rightChild)) + 1
        
        return tempLeftNode
    
    #rotate left
    def rotateLeft(self,node):
        print("Rotating to the right on node",node.data)
        tempRightNode = node.rightChild
        t = tempRightNode.leftChild
        tempRightNode.leftChild = node
        node.rightChild = t
        #update height
        node.height = max(self.calcHeight(node.leftChild),self.calcHeight(node.rightChild)) + 1
        tempRightNode.height = max(self.calcHeight(tempRightNode.leftChild),self.calcHeight(tempRightNode.rightChild)) + 1
        return tempRightNode
        
    #insert node helper Method
    def insert(self,data):
        self.root = self.insertNode(data,self.root)
    
    def insertNode(self,data,node):
        if not node:
            return Node(data)
        if data < node.data:
            node.leftChild = self.insertNode(data,node.leftChild)
        else:
            node.rightChild = self.insertNode(data,node.rightChild)
        node.height = max(self.calcHeight(node.leftChild),self.calcHeight(node.rightChild)) + 1
        
        return self.settleViolation(data,node)
        
    def settleViolation(self,data,node):
        balance = self.calcBalance(node)
        
        #case 1: left left heavy situation
        if balance>1 and data < node.leftChild.data:
            print("Left Left heavy situation")
            return self.rotateRight(node)
            
        #case 2: Right right heavy situation
        if balance<-1 and data > node.rightChild.data:
            print("Right right heavy situation")
            return self.rotateLeft(node)
            
        #case 3: Left Right heavy situation
        if balance>1 and data>node.leftChild.data:
            print("Left right heavy situation")
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)
            
        #case 4: Right Left heavy situation
        if balance<-1 and data<node.rightChild.data:
            print("Right left heavy situation")
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)
        
        return node
        
    #remove helper method
    def remove(self,data):
        if self.root:
            self.root = self.removeNode(data,self.root)
        
    def removeNode(self,data,node):
        if not node:
            return node
        if data<node.data:
            node.leftChild = self.removeNode(data,node.leftChild)
        elif data>node.data:
            node.rightChild = self.removeNode(data,node.rightChild)
        else:
            #case 1: it's leaf node
            if not node.leftChild and not node.rightChild:
                print("Removing a leaf node...");
                del node
                return None
            #case 2: it has a single child 
            if not node.leftChild:
                print("Removing a node with single right child..");
                tempNode = node.rightChild
                del node
                return tempNode
            elif not node.rightChild:
                print("Removing a node with single left child..")
                tempNode = node.leftChild
                del node
                return tempNode
            else:
                pass
            #case 3: it has 2 children
            print("Removing a node with two children...")
            tempNode = self.getPredecessor(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.removeNode(tempNode.data,node.leftChild)
            
        if not node:
            return node #if the tree had just a single node
        node.height = max(self.calcHeight(node.leftChild),self.calcHeight(node.rightChild)) + 1
            
        balance = self.calcBalance(node)
        
        #doubly left heavy situation...
        if balance>1 and self.calcBalance(node.leftChild)>=0:
            return self.rotateRight(node)
            
        #left right heavy situation..
        if balance>1 and self.calcBalance(node.leftChild)<0:
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)
            
        # doubly right heavy situation
        if balance<-1 and self.calcBalance(node.rightChild)<=0:
            return self.rotateLeft(node)
            
        #right left heavy situation
        if balance<-1 and self.calcBalance(node.rightChild)>0:
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)
            
        return node
    
    def getPredecessor(self,node):

        if node.rightChild:
            return self.getPredecessor(node.rightChild);
        return node;
        
        
    #Traverse helper Method
    def traverse(self):
        if self.root:
            self.traverseInorder(self.root)
            
    def traverseInorder(self,node):
        if node.leftChild:
            self.traverseInorder(node.leftChild)
            
        print("%s" %node.data)
        
        if node.rightChild:
            self.traverseInorder(node.rightChild)

avl = AVL();
avl.insert(1)
avl.insert(2)
avl.insert(3)
avl.insert(4)
avl.insert(5)
avl.insert(6)

avl.traverse()
avl.remove(4)
avl.traverse()
    
    
