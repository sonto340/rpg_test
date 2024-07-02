import random
numbers = [2, 1, 3, 1, 2]
x = 2 # I plan to import x from a dict with various values. This works as expected, aside 

print(numbers)
print(numbers[x]) #shows the value expected upon print
random.shuffle(numbers) 
print(numbers) #shows the shuffled list
print(numbers[x]) #this pulls the original value from the list at index (x) before being shuffled