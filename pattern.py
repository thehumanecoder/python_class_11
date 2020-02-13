alphabet = str(input("Enter the alphabet you want to print in the pattern : "))
count = 0
for i in range(6) :
        print(alphabet,end=" ")
print("\n")

for m in range(4):    
    for j in range(6):
        count = count+1
        if count is 3 or count is 4 or count is 9 or count is 10 or count is 15 or count is 16 or count is 21 or count is 22:
            print(alphabet,end=" ")
        else:
            print(" ",end=" ") 
    print("\n")

print("\n")
for i in range(6) :
        print(alphabet,end=" ")


