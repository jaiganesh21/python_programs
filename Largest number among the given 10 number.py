lst = []

num = int(input('give the count of number :'))

for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)

print("Largest number in list :", max(lst))