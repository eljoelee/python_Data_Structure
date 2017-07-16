# -*- coding: utf-8 -*-
'''
리스트 a, 찾는 값 x, 위치 i
'''
def search_list(a, x):
    n = len(a)
    for i in range(0, n):
        if x == a[i]:
            return i
    return -1

def search_list_all(a, x):
    n = len(a)
    arr = []
    for i in range(0, n):
        if x == a[i]:
            arr.append(i)
    return arr

if __name__ == '__main__':
    v = [17, 92, 18, 33, 58, 7, 33, 42]
    print(search_list(v, 18))
    print(search_list_all(v, 33))
    print(search_list_all(v, 900))
    print(search_list(v, 900))