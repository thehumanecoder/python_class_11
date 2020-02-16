
def f(x):
    d = 0
    while x>=1:
        (x,d) = (x/5,d+1)
        
    print(d)
    return(d)

op = f(4000)
print(op)