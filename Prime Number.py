num = int(input("Enter the number :"))
for i in range(2, num):
    if num % i == 0:
        print(num, "not a prime")
        break
else:
    print(num, "prime")
