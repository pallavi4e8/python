x="madam"
l=0
r=len(x)-1
while l<r:
    if x[l]==x[r]:
        l+=1
        r-=1
        print("palindrom")
    else:
        print("not a palindrom")
