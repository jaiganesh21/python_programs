rows = int(input("Enter the rows : "))
cols = int(input("Enter the columns : "))

mat1 = []
mat2 = []

print("Matrix 1")
for i in range(rows):
    temp = []
    for j in range(cols):
        temp.append(int(input("Enter value " + str(i) + str(j))))
    mat1.append(temp)

print("Matrix 2")
for i in range(rows):
    temp = []
    for j in range(cols):
        temp.append(int(input("Enter value " + str(i) + str(j))))
    mat2.append(temp)

print(mat1)
print(mat2)

