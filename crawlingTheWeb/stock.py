import re
import urllib.request

arrayofStock = ['FB','GOOGL','DATA','BABA','GOOG']

for i in arrayofStock:
    url = "http://stocktwits.com/symbol/"
    stock=i
#stock=input("Enter your stock: ")
    url = url + stock

    data = urllib.request.urlopen(url).read()

    data1 = data.decode("utf-8")
    m = re.search('"isFollowing":false,"price":',data1)
    start=m.end()
    n=re.search(',"open":',data1)
    end=n.start()
#print(m)
#print(n)
    final = data1[start:end]
    print("The stock value of "+str(stock.upper())+" "+final)
