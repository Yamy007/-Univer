task = input("1 - fb, 2 - while: ")
if task == "1":
    print("before")
    list_fb = [1,2]
    for i in range(50):
            list_fb.append(list_fb[-1]+list_fb[-2])
    print(list_fb)
    print("after")
    new_list_fb = []
    for i in range(4, 20):
        new_list_fb.append(list_fb[i])
    print(new_list_fb)
if task == "2":
    list = []
    for i in range(0, 21):
        if i %2 == 0:
            list.append(i)
    print(list)
    list_2 = []
    a= -1
    while a > -21:
        list_2.append(a)
        a-=3
    print(list_2)
