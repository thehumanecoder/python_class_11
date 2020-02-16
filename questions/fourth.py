def h(n):
    s = 0
    for i in range(2,n):
        if n%i == 0:
            s = s+i
    return(s)

def f(n):
    s = 0
    for i in range(2,n):
        if n%i == 0:
            s = s+i
    return(s)

op = h(36)-f(34)
print(op)
