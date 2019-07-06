#FIFO

class Queue:

    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enqueue(self,data):
        self.queue.append(data)

    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data

    def sizeQueue(self):
        return len(self.queue)

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)

print("Queue:"+str(queue.queue))

print("Dequeued element: "+str(queue.dequeue()))
print("Size of queue: "+str(queue.sizeQueue()))

print("Queue is empty: "+str(queue.isEmpty()))
print("Queue:"+str(queue.queue))
