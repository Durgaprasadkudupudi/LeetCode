def binary(arr,n):
    low=0
    high=n-1
    ans=float('inf')
    while(low<=high):
        mid=(low+high)//2
        if arr[low]<=arr[mid]:
            ans=min(ans,arr[low])
            low=mid+1
        else:
            ans=min(ans,arr[mid])
            high=mid-1
    return ans
arr=[4,5,6,7,0,1,2] 
n=len(arr)
a=binary(arr,n)
print(a)

def binary(arr,n):
    low=0
    high=n-1
    fin=0
    ans=float('inf')
    while(low<=high):
        mid=(low+high)//2
        if arr[low]<=arr[mid]:
            ans=min(ans,arr[low])
            low=mid+1
        else:
            ans=min(ans,arr[mid])
            high=mid-1
    fin=arr.index(ans)
    print(fin)
arr=[1,2,4,5,6]
n=len(arr)
binary(arr,n)
    