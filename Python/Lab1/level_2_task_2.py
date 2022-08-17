try:
    x = int(input("Please enter number(1-9): "))
    if x  >=1 and x <=3:
        s = input("PLease enter line: ")
        n = input("Please repetition of lines: ")
        list = []
        list.append(s) #can delete if you want have only n repetition, if you stay this you have n+1 repetition
        for i in range(0, int(n)):
            list.append(s)
        print("Result: ",list)
    elif x>=4 and x<=6:
        m = input("Please enter power: ")
        print("Result: ",pow(x, int(m)))
    elif x>=7 and x<=9:
            for i in range(11):
                x +=1
                print("Result: ",x)
    else:
        print("Error input :(")

except:
    print("Error input!")
