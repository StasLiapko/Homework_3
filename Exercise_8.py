a = int(input("Input side a "))
b = int(input("Input side b "))
c = int(input("Input side c "))
if (a+b) > c and (a+c) > b and (b+c) > a:
    print(True)
else:
    print(False)
