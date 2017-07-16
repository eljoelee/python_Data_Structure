def findSameName(a):
    result = set()

    for i in range(0, len(a)-1):
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                result.add(a[i])
    return result

if __name__ == '__main__':
    name = ['Tom', 'Jerry', 'Mike', 'Tom']
    print(findSameName(name))