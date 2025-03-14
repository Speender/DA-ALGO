def find_pattern(text, pattern):
    result = []
    n, m = len(text), len(pattern)

    for i in range(n - m + 1):
        if text[i:i + m] == pattern: 
            result.append(i)

    return result

if __name__ == "__main__": #optional
    text = "ABCABCD"
    pattern = "ABC"
    print("Pattern found at indices:", find_pattern(text, pattern))
