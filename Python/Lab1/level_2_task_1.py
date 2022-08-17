import math
def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n
task = input("2 - rectangle, 3 -  triangle, 4 - calculate: ")
if task == "2":
    width = input("Enter width rectangle: ")
    height = input("Enetr height rectangle: ")
    chose = input("1 - area, 2 - perimetr: ")
    if chose  == "1":
        try:
            print("Result: ", float(width)*float(height))
        except:
            print("you write  bad  request :(")
    elif chose == "2":
        try:
            print("Result: ", float(width)*2 + float(height)*2)
        except:
            print("you write  bad  request :(")
    else:
        print("you write  bad  request :(")
elif task == "3":
    a_h = float(input("Enter a, where a is the side of the triangle: "))
    b_h = float(input("Enter b, where b is the side of the triangle: "))
    c_h = float(input("Enter c, where c is the side of the triangle: "))
    try:
        if a_h == 0 or b_h == 0 or c_h == 0:
            print("a side of a triangle cannot be 0")

        elif a_h+b_h < c_h or a_h+c_h < b_h or c_h+b_h < a_h:
            print("such a triangle does not exist because the sum of two sides must be greater than the third side")
        else:

            p = (a_h+b_h+c_h)/2
            print("Result: h(a)", 2/a_h*math.sqrt(p*(p-a_h)*(p-b_h)*(p-c_h)))
            print("Result: h(b)", 2/b_h*math.sqrt(p*(p-a_h)*(p-b_h)*(p-c_h)))
            print("Result: h(c)", 2/c_h*math.sqrt(p*(p-a_h)*(p-b_h)*(p-c_h)))
    except:
        print("You entered invalid values")
elif task== "4":
    x_1 = 1.45
    y_1 = -1.22
    z = 3.5
    x_2 = 1.2
    y_2 = -0.8
    z_2 =  (math.sin(pow(x_2, 3)))+math.pow(math.cos(y_2), 2)
    b = 1 + (z**2)/(3+(z**2)/5)
    print("Result a: ", (2* math.cos(x_1 - math.pi/6)*b)/((1/2)+math.sin(y_1)**2))
    print("Result s: ", 1+x_2+(x_2**2/fac(2))+(x_2**3/fac(3))+(x_2**4/fac(4)))


