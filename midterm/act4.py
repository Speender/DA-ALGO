class Item:
    def __init__ (self, weight, value):
        self.weight = weight
        self.value = value
def getMax(weights, values, capacity):
    items = [Item(w,v) for w,v in zip (weights, values)]

    items.sort(key = lambda item: item.value / item.weight, reverse = True)

    maxVal = 0.0

    for item in items:
        if capacity >= item.weight:
            maxVal += item.weight
            capacity -= item.weight
        else:
            maxVal += (item.value / item.weight) * capacity
            break
    return maxVal
if __name__ == "__main__":
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50

    print("Maximum value:", getMax(weights, values, capacity))