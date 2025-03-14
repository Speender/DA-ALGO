#Dynamic
def lcs(x, y):
    table = [0] * len(x)
    res = 0
    
    for i in y:
        curr = 0
        for index, value in enumerate(table):
            if curr < value:
                curr = value
            elif i == x[index]:
                table[index] = curr + 1
                res = max(res, curr + 1)
    return res
#Brute Force
def NaiveSearch(str, pat):
    res = []
    x = len(str)
    y = len(pat)

    for i in range (x - y + 1):
        if str[i : i + y] == pat:
            res.append(i)
#Binary Search
def BinarySearch(arr, left, right, target):
    if left > right:
        return -1
    
    mid = left + (right - left) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return BinarySearch(arr, left, mid - 1, target)
    else:
        return BinarySearch(arr, mid + 1, right, target)
#Knacpsack
class Item:
    def __init__ (self, weight, value):
        self.weight = weight 
        self.value = value 
def getMax(weights, values, capacity):
    items = [Item(w,v) for w,v in zip(weights,values)]

    items.sort(key = lambda item: item.value / item.weight, reverse=True)

    maxVal = 0.0

    for item in items:
        if capacity >= item.weight:
            maxVal += item.value
            capacity -= item.weight
        else:
            maxVal += (item.value / item.weight) * capacity
            break
    return maxVal
if __name__ == "__main__": #optional
    x = "ABCBDAB"
    y = "BDCAB"
    print("============Dynamic==========")
    print(lcs(x, y))
    print("=============================")
    print("========BRUTE FORCE==========")
    text = "ABCABCD"
    pattern = "ABC"
    print("Pattern found at indices:", NaiveSearch(text, pattern))
    print("==============================")
    print("========BINARY SEARCH=========")
    arr = [1,2,3,4,5,6,7,8,9,10]
    target = 6
    result = BinarySearch(arr, 0, len(arr) - 1, target)
    print(f"{result}")
    print("==============================")
    print("=====FUNCTIONAL KNAPSACK======")
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50

    print("Maximum value:", getMax(weights, values, capacity))