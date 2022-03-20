n = int(input("Enter number of rows: "))

for i in range(n, 0, -1):
    for j in range(0, i):
        print("* ", end=" ")
    print()