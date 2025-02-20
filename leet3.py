def binarylower(arr,target,n):
    low=0
    high=n-1
    ans=n
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]>=target):
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
def binaryupper(arr,target,n):
    low=0
    high=n-1
    ans=n
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]>target):
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans

arr=[1,2,3,4,5,5,6,8]
target=8
n=len(arr)
lb=binarylower(arr,target,n)
if lb==n or arr[lb]!=target:
    print(-1) 
else:
    print("element found at index : ",lb,binaryupper(arr,target,n)-1)
