def student_search(sno, sname, x):
    n = len(sno)
    for i in range(0, n):
        if x == sno[i]:
            return sname[i]
    return "?"

if __name__ == '__main__':
    sno = [39, 14, 67, 105]
    sname = ["Justin", "John", "Mike", "summer"]

    print(student_search(sno, sname, 14))
    print(student_search(sno, sname, 1))