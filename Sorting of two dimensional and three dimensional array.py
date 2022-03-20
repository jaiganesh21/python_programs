size = int(input())
array_input = []
for x in range(size):
    array_input.append([int(y) for y in input().split()])
    array_input.sort()
print(array_input)
