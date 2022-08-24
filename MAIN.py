# just do 8 sets of for i in 62
import keyboard as k
import time as t


t.sleep(2)
b = 100
while(True):
    #----
    l = [10,10,10,10,10,10,0,0]
    for i in range(b):
        l[0] += 1
        for j in range(len(l)):
            if(l[j] == 62):
                l[j] = 0
                if(j+1 == len(l)):
                    l.append(0)
                else:
                    l[j+1] += 1
    #----
    s = []
    for i in range(len(l)):
        if(l[i] >= 0 and l[i] <= 9):
            s.append(chr(l[i]+48))
        elif(l[i] > 9 and l[i] <= 36):
            s.append(chr(l[i]+55))
        elif(l[i] > 36 and l[i] <= 62):
            s.append(chr(l[i]+61))
    #----
    # k.write(s)
    # k.press_and_release('enter')
    print(s, " -- ", b)
    b += 1
    # t.sleep(1)

# l = [0]
# for i in range(9+4):
#     l[0] += 1
#     for j in range(len(l)):
#         if(l[j] == 62):
#             l[j] = 0
#             if(j+1 == len(l)):
#                 l.append(0)
#             else:
#                 l[j+1] += 1
# s = []
# for i in range(len(l)):
#     if(l[i] >= 0 and l[i] <= 9):
#         s.append(chr(l[i]+48))
#     elif(l[i] > 9 and l[i] <= 36):
#         s.append(chr(l[i]+55))
#     elif(l[i] > 36 and l[i] <= 62):
#         s.append(chr(l[i]+61))
# print(l)
# print(s)
