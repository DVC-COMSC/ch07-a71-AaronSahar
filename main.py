average = 0
inputvalues = input('Enter all elements values: ')
numbers = inputvalues.split()
for i in range(len(numbers)):
	numbers[i] = int(numbers[i]) 
for i in range(10):
    average += numbers[i]
average /= 10
for i in range(10):
    numbers[i] -= average
    if numbers[i] < 0:
        numbers[i] *= -1
for i in range(10):
    print(f'{numbers[i]:.2f}', end=' ')