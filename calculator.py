
def mango(x,y):
    return x+y
def orange(x,y):
    return x-y
def banana(x,y):
    return x*y
def jackfruit(x,y):
    return x/y
def cherry(x,y):
    return x%y

def main():
    a = int(input("Enter the first number : "))
    b = int(input("Enter the second numver :  "))
    print("Enter 1 for Addition")
    print("Enter 2 for Substraction")
    print("Enter 3 for Multiplication")
    print("Enter 4 for Division")
    print("Enter 5 for Reminder")
    c = int(input("Enter your choice : "))
    
    
    if c is 1:
        print(mango(a,b))
    elif c is 2:
        print(orange(a,b))
    elif c is 3:
        print(banana(a,b))
    elif c is 4:
        print(jackfruit(a,b))
    elif c is 5:
        print(cherry(a,b))


if __name__ == "__main__": 
    main()

