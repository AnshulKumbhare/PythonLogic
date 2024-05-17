flag = True

for i in range(4):
    num = None
    if flag :
        num = 1
    else:
        num = 0
    for j in range(i + 1):
        print(num, end="  ")
        if num == 1:
            num = 0
        else:
            num = 1
    print()
    if flag:
        flag = False
    else:
        flag = True
