list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a  = 2
b = 8



result = 1
for i in list:
    if i > a and i <b:
        result *=i
print(result)

c = 1
result_while = 1
while c < len(list):

    if   list[c-1] >a  and list[c-1]< b:
        result_while*=c
    c+=1
print(result_while)

