def selection_sort(n):
    for i in range(len(n)-1):
        p = i
        for j in range(i+1, len(n)-1):
            if n[j] < n[p]:
                p = j
        n[i], n[p] = n[p], n[i]

n = [111,2,4,777,567,987,5,7,6,100]
print(n)
selection_sort(n)

print(n)