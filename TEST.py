s = []
for i in range(62):
    if(i >= 0 and i <= 9):
        s.append(chr(i+48))
    elif(i > 9 and i <= 35):
        s.append(chr(i+55))
    elif(i > 35 and i <= 62):
        s.append(chr(i+61))
    print(i, s[i])