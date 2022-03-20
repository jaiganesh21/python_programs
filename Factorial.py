num = int(input("Enter a number:"))
f = 1

if num < 0:
   print("factorial does not have negative numbers")

elif num == 0:
   print("The factorial of",num,"is",f)

else:
   for i in range(1,num + 1):
       f = f*i
   print("The factorial of",num,"is",f)
