import heapq

class Node:
    def __init__(self,name,frequency):
        self.name = name
        self.frequency = frequency
        self.left = None
        self.right = None
        
    # based on min frequency property heap will be maintained     
    def __lt__(self,other):
        selfPriority = self.frequency
        otherPriority = other.frequency
        return selfPriority < otherPriority
        
class HuffMan:
    
    def __init__(self):
        self.head = None;
        self.size = 0;
        self.charArray = []
        
    def insert(self,name,frequency):
        self.charArray.append(Node(name,frequency))
        
    def algorithm(self):
        a = []
        bitsRequired = 0;
        
        for x in self.charArray:
            heapq.heappush(a,x)
        
        while len(a)>1:
            node = Node("Z",0)
            node.left = heapq.heappop(a)
            node.right = heapq.heappop(a)
            node.frequency = node.left.frequency + node.right.frequency
            a.append(node)
            bitsRequired = node.frequency
        print("Bits Required after HuffMan Compression: "+ str(bitsRequired))  
            
        


hf = HuffMan();
hf.insert("d",16);
hf.insert("b",13);
hf.insert("c",12);
hf.insert("e",9);
hf.insert("f",5);
hf.insert("a",45);
hf.algorithm();

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
