def binary(arr, n, target):
    low = 0
    high = n - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        # If the element is found
        if arr[mid] == target:
            return mid
        
        
        # Check if the left half is sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= target <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:  # Right half must be sorted
            if arr[mid] <= target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
                
    return -1  # Element not found

arr = [4, 5, 1, 2, 3]
target = 3
n = len(arr)

print(binary(arr, n, target))  # Output: 0
