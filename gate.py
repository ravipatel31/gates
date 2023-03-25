def AND(x,y):
    z=x and y
    print("Output=",z)
    
def OR(x,y):
    z=x or y
    print("Output=",z)
def NOT(x):
    z=~x+2
    print("Output=",z)
    

print("1.AND")
print("2.OR")
print("1.NOT")
ch=int(input("ENter a choice: "))

if ch==1:
    x=int(input("ENter the input of x(0 or 1): "))
    y=int(input("ENter the input of x(0 or 1): "))
    AND(x,y)
if ch==2:
    x=int(input("ENter the input of x(0 or 1): "))
    y=int(input("ENter the input of x(0 or 1): "))
    OR(x,y)
if ch==3:
     x=int(input("ENter the input of x(0 or 1): "))
     NOT(x)