
numbers = [1,2,300,4,5]

# random indexing --> O(1) get items if we know the index!!
print(numbers[1]);

#numbers[1] = 'Adam'

print(numbers[1]);

for num in numbers:
    print(num);

for i in range(len(numbers)):
    print(numbers[i]);

print(numbers[0:2]);

print(numbers[:]);

print(numbers[:-1]);

# find maximum numbers: O(n) search running time.
maximum = numbers[0];
for num in numbers:
    if num > maximum:
        maximum = num;
print(maximum);
