import time,random

def numPrint(max):
    file1=open("numPrint.txt","w+")
    time1 = time.time()
    for i in range(0,max):
        #print(i)
        file1.write(str(random.randint(0,max))+"\n")
    time2 = time.time()
    print("Time taken: "+str(time2-time1))
    file1.seek(0,0)
    lines = [line.rstrip('\n') for line in open('numPrint.txt')]
    #list=file1.read()
    print(lines)
    
# call function like numPrint(100) in shell
