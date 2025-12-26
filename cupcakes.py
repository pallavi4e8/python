'''you are given an array A of size N,where each element represenets the number of cupcakes sold in a single transaction.your task is to find and return an integer value representing the sum of the cupcakes from the transacions where 5 or more cupcakes were sold
return0 if there is no transaction with more than 5 cupcakes sold. '''
def cupcakes(n,arr):
    sum=0
    for i in range (n):
        if arr[i]>=5:
            sum+=arr[i]
    print(sum)
n=5
arr=[1,2,5,8,3,7]
cupcakes(n,arr)
            
            
            
