def h(m,n):
    s = 0
    while m>=n:
        (s,m)=(s+1,m/n)
    return(s)
op = h(637,4)
print(op)