def gcd(a,b):
    i = min(a,b)

    while i >= 1:
        if a % i == 0 and b % i ==0:
            return i
        i -= 1
def easyGcd(a, b):
    if b == 0:
        return a
    return easyGcd(b, a%b)

print(gcd(1, 5))
print(gcd(3, 6))
print(easyGcd(60, 24))