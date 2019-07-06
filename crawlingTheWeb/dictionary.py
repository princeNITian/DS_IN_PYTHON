import re
import urllib.request

url = "http://www.dictionary.com/browse/"

word= input("Enter the word: ")
url = url + word

try:
    data = urllib.request.urlopen(url).read()

    data1 = data.decode("utf-8")
#print(data1)

    m = re.search('meta name="description" content="',data1)
    start = m.end()
    end = start + 300

    string = data1[start:end]
#print(string)

    m1 = re.search('See more.',string)
#print(m1)
    end1 = m1.start()-1

    string1 = string[:end1]
    print(string1)
except:
    print("I'm sorry. your word in not in the dictionary.")
