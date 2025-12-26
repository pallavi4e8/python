'''n=int(input())
org=n
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
    if rev==org:
        print("palindrome")
    else:
        print("not palindrome")'''

    
x=int(input())
if x%5==0:
    if x%2==0:
        print("yes")
    else:
        print("not satisfied")
else:
        print("no")
        
