import functools

def add(a, b):
    return a + b

res1 = add(4, 2)
print(res1)

plus3 = functools.partial(add, 3)
plus5 = functools.partial(add, 5)

res2 = plus3(2)
res4 = plus5(4)

print(res2)
print(res4)