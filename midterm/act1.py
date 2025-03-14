def lcs(x,y):
    table = [0] * len(x)
    res = 0

    for i in y:
        curr = 0
        for index, val in enumerate(table):
            if curr < val:
                curr = val
            elif i ==x[index]:
                table[index] = curr + 1
                res = max(res, curr + 1)
    return res
x = "ABCBDAB"
y = "BDCAB"

print(lcs(x, y))