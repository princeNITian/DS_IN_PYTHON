class Heap(object):
    HEAP_SIZE = 10
    def __init__(self):
        self.heap = [0]*Heap.HEAP_SIZE
        self.currentPos = -1

    def insert(self,data):
        if self.isFull():
            print("Heap is already Full. %d Discarded." % data)
            return
        self.currentPos += 1
        self.heap[self.currentPos] = data
        self.fixUp(self.currentPos)
    def isFull(self):
        if self.currentPos == self.HEAP_SIZE - 1:
            return True
        else:
            return False
    def fixUp(self, index):

        pIndex = int((index-1)/2)

        while pIndex >=0 and self.heap[index] > self.heap[pIndex]:
            temp = self.heap[index]
            self.heap[index] = self.heap[pIndex]
            self.heap[pIndex] = temp
            index = pIndex
            pIndex = int((index-1)/2)

    def delete_root(self):
        if self.isEmpty():
            print("Heap is Empty!!")
            return
        maxValue = self.heap[0]
        self.heap[0]=self.heap[self.currentPos]
        self.heap[self.currentPos] = maxValue
        self.currentPos -= 1
        self.fixDown(0)
        return maxValue

    def fixDown(self, index):
        k = self.heap[index]
        lChild = 2*index + 1
        rChild = 2*index + 2
        while rChild <= self.currentPos:
            if k >= self.heap[lChild] and k > self.heap[rChild]:
                self.heap[index]= k
                return
            else:
                if self.heap[lChild] > self.heap[rChild]:
                    self.heap[index] = self.heap[lChild]
                    index = lChild
                else:
                    self.heap[index] = self.heap[rChild]
                    index = rChild
            lChild = 2*index +1
            rChild =  2*index+2

            # If number of nodes is even
        if lChild == self.currentPos and k < self.heap[lChild]:
            self.heap[index] = self.heap[lChild]
            index = lChild
        self.heap[lChild] = k

    def isEmpty(self):
        if self.currentPos == -1:
            return True
        else:
            return False
        
    def display(self):
        if self.currentPos == 0:
            print("Heap is empty")
        print("Heap size = ", self.currentPos+1)
        for i in range(0,self.currentPos+1):
            print(self.heap[i]," ",end = ' ')
        print()

heap = Heap()
heap.insert(5)
heap.insert(15)
heap.insert(50)
heap.insert(25)
heap.insert(4)
heap.insert(12)
heap.insert(20)
heap.insert(33)
heap.insert(-40)
heap.insert(90)
heap.insert(555)
heap.display()
heap.delete_root()
heap.display()
