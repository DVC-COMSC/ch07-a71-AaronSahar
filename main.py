list = []
average = 0
for i in range(10):
    list.append(int(input("Enter a number")))
    average += list[i]
average /= 10
for i in range(10):
    list[i] -= average
    if list[i] < 0:
        list[i] *= -1
for i in range(10):
    print(f'{list[i]:.2f}', end=' ')
print(average)
