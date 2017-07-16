def find_max(a):
    n = len(a)
    max_v = a[0]
    for i in range(1, n):
        if a[i] > max_v:
            max_v = a[i]
    return max_v

def find_max_pos(a):
    n = len(a)
    max_idx = 0
    for i in range(1, n):
        if a[i] > a[max_idx]:
            max_idx = i
    return max_idx

def find_min_pos(a):
    min_idx = 0
    for i in range(1, len(a)):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx

def find_max_recursively(a, n):
    if n == 1:
        return a[n-1]
    else:
        max = find_max_recursively(a, n-1)
        current = a[n-1]
        if  max > current:
            return max
        else:
            return current

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_max(v))
print(find_max_pos(v))
print(v[find_min_pos(v)])
print(find_max_recursively(v, 8))