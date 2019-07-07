
class Stack:

    def __init__(self):
        self.stack = [];

    def isEmpty(self):
        return self.stack == []

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        return self.stack[-1]

    def sizeStack(self):
        return len(self.stack)

    #stored data into stack
    def bucket(self):
        print('Stack data from top is : ')
        self.stack.reverse()
        for x in self.stack:
            print("| "+str(x)+" |")
            print(" ___")
        print('****************')
        self.stack.reverse()


stack = Stack();

stack.push(1);
stack.push(2);
stack.push(3);
stack.bucket()
print("Size of Stack: "+ str(stack.sizeStack()));
print("Popped: ",stack.pop())
stack.bucket()
print("Popped: ",stack.pop())
stack.bucket()
print(stack.sizeStack())
print("Peek ",stack.peek())
print("Size of Stack: "+ str(stack.sizeStack()));
