# Ask for user input
a=float(input("enter side a:"))
b=float(input("enter side b:"))
c=float(input("enter side c:"))
# Triangle Inequality Theorem
if (a+b>c)and (a+c>b) and (b+c>a):
    print ("this is a valid triangle .")
else:
    print ("this is not a valid triangle.")

