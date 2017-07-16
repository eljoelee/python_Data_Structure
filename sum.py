def sum_n(n):
    s = 0
    for i in range(1, n+1):
        s+=i
    return s

def sum_n2(n):
    return n * (n+1) // 2

def exam1(n):
    s = 0
    for i in range(1, n+1):
        s += (i*i)
    return s

def recurSum(n):
    if n <= 1:
        return 1
    return n + recurSum(n-1)

if __name__ == '__main__':
    print(sum_n(10))
    print(sum_n2(100))
    print(recurSum(10))
    print(exam1(10))