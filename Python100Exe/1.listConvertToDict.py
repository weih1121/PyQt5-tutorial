def ListToDict(list1, list2):
    if len(list1) != len(list2):
        print("两个list长度不相等")
    else:
        tmp = dict(zip(list1, list2))

    return tmp


def ListToDict1(list1, list2):
    tmp = {}
    if len(list1) != len(list2):
        print("两个list长度不相等")
    else:
        for i in range(len(list1)):
            tmp.setdefault(list2[i], list1[i])

    return tmp



list1 = [1, 2, 3]
list2 = ['x', 'y', 'z']

print(ListToDict(list2, list1))
print(ListToDict1(list1, list2))



