def power_concat(a, b):
    c = []
    for item in a:
        if item not in c:
            c.append(item)
    for item in b:
        if item not in c:
            c.append(item)
    return len(c)

def differ(a, b):
    c = a.copy()
    for item in b:
        if item in c:
            c.remove(item)
    return c

def power_outer(a, b):
    t1 = differ(a, b)
    t2 = differ(b, a)
    c = []
    for i in t1:
        c.append(i)
    for i in t2:
        c.append(i)
    return len(c)