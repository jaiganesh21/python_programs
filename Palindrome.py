n=int(input("Enter a value:"))
temp=n
r=0
while(n>0):
    p=n%10
    r=r*10+p
    n=n//10
if(temp==r):
    print("The number is palindrome! ")

else:
    print("The number is Not a palindrome! ")
