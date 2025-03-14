def BinarySeach(arr, left, right, target):
    if left > right:
        return -1
    
    mid = left + (right - left) //2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return BinarySeach(arr, left, mid - 1, target)
    else:
        return BinarySeach(arr, mid + 1, right, target)
    
arr = [1,2,3,4,5,6,7,8,9,10]
target = 6
result = BinarySeach(arr, 0, len(arr) - 1, target)
print(f"{result}")