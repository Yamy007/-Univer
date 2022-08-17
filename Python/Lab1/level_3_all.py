task = input("1 - task_1, 2 - task_2, 3 - task_3: ")

if task == "1":
    x = 2
    y = 6
    print(x< y and y%x==0)
    print(x * y == 12   and  y//x==3)
    print(x>y and y-x == 5)
    print(x<y and x*y==100)


    print(x < y or x>y)
    print(x*y == 12 or x+y == 44545)
    print(x*20 == y *5 or  x >y)
    print(x+y == y-x or x*y==y/x)


    if True:
        print("hello world")

    f = open('python.txt', 'w')
    f.write("Programming is fun "+"\n"+"When the work is done")
    f.close()


elif task == "2":
    try:
        x = int(input("Enter your number: "))
        def func():
            if x%2 == 0:
                print("this number is even")
            else:
                print("this number isn't even")
        func()
    except:
        print("bad request :(")

elif task == "3":
    school = dict(a_1 = 20, b_1 = 30, a_2 = 24, a_4 = 25, b_4 = 31, a_6 = 12, b_7= 18, a_9=20, a_10 = 18, b_11 = 18)
    chose = input("1 - all class, 2 - edit class, 3- add class, 4 - delete class")
    if chose == "1":
        print(school)
    if chose == "2":
        seletct = input("enter class: ")
        select = int(input("enter new value: "))
        school[seletct] = select
        print(school)
    if chose == "3":
        seletct = input("enter class: ")
        select = int(input("enter  value: "))
        school[seletct] =  select
        print(school)
    if chose == "4":
        seletct = input("enter class: ")
        del school[seletct]
        print(school)


