a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))
c = int(input("Enter a third number: "))

if (a >= b and a <= c) or (a >= c and a <= b):
    print(a)
elif (b >= a and b <= c) or (b >= c and b <= a):
    print(b)
else:
    print(c)
