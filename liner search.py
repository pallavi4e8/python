def liner_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
arr=list(map(int,input().split(",")))
target=int(input())
print(liner_search(arr,target))
