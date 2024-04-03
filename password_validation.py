import re

pwd = input("Enter Password: ")

flag = True

while flag:
    if (len(pwd) < 6) and (len(pwd) > 16):
        break
    elif not re.search('[a-z]', pwd):
        break
    elif not re.search('[A-Z]', pwd):
        break
    elif not re.search('[0-9]', pwd):
        break
    elif not re.search('[$#@]', pwd):
        break
    elif re.search(" ", pwd):
        break
    else:
        print("Valid Password")
        flag = False
        break


if flag:
    print("Not a valid Password.")