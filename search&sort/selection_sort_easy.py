def find_min_idx(a):
    n = len(a)
    min_idx = 0
    for i in range(1, n):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx

def sel_sort(a):
    result = [] # 새 리스트를 만들어 정렬된 값 저장
    while a: # 주어진 리스트에 값이 남아 있는 동안 계속
        min_idx = find_min_idx(a)
        value = a.pop(min_idx)
        result.append(value)
    return result

if __name__ == '__main__':
    d =[2, 4, 5, 1, 3]
    print(sel_sort(d))