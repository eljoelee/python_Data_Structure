def findCouple(a):
    result = []
    for i in range(0, len(a)-1):
        for j in range(i+1, len(a)):
            result.append(a[i] + " - " + a[j])
    return result


if __name__ == '__main__':
    name = ['Tom', 'Jerry', 'Mike', 'John']
    print(findCouple(name))