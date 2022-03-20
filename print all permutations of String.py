from itertools import permutations

string = "abc"
a = permutations(string)

for i in a:
    # ans = str(i)[2:-2].replace(",", "").replace("'", "").replace(" ", "")
    ans2 = "".join(i)
    print(ans2) # (a, b, c)