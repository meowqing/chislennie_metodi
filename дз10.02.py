def concat(a, b):
    c = []
    for item in a:
        if item not in c:
            c.append(item)
    for item in b:
        if item not in c:
            c.append(item)
    return c

def intersect(a, b):
    c = []
    if len(a) > len(b):
        a, b = b, a
    for item in a:
       if item in b:
           c.append(item)
    return c

def differ(a, b):
    c = a.copy()
    for item in b:
        if item in c:
            c.remove(item)
    return c

def outer(a, b):
    t1 = differ(a, b)
    t2 = differ(b, a)
    c = []
    for i in t1:
        c.append(i)
    for i in t2:
        c.append(i)
    return c

a = [1, 2, 3, 4, 5]
b = [2, 5, 7, 10, 12]

print(concat(a, b))
print(intersect(a, b))
print(differ(a, b))
print(differ(b, a))
print(outer(a, b))