import keyboard as k
import time as t
print(3)
t.sleep(1)
print(2)
t.sleep(1)
print(1)
t.sleep(1)
print("GO")
# l = [0,0,0,0,0,0,0,0]
# for q in range(61):
#     for w in range(61):
#         for e in range(61):
#             for r in range(61):
#                for o in range(61):
#                     for y in range(61):
#                         for u in range(61):
#                             for i in range(61):
#                                 l[0] += 1
#                                 for j in range(len(l)):
#                                     if(l[j] == 62):
#                                         l[j] = 0
#                                         if(j+1 == len(l)):
#                                             l.append(0)
#                                         else:
#                                             l[j+1] += 1
#                                 s = []
#                                 for i in range(len(l)):
#                                     if(l[i] >= 0 and l[i] <= 9):
#                                         s.append(chr(l[i]+48))
#                                     elif(l[i] > 9 and l[i] <= 35):
#                                         s.append(chr(l[i]+55))
#                                     elif(l[i] > 35 and l[i] <= 62):
#                                         s.append(chr(l[i]+61))
#                                 # k.write(s)i0000000
#                                 # k.press_and_release('enter')
#                                 print(s)
#                                 t.sleep(1)
# Tried a for i in range (8) for i in range (61)
# That didn't work but this one does
# Issue earlier was where I started and probably the while statement
# Doesn't matter cause I have no use for this code now
c = 1
l = [0,0,0,0,0,0,0,0,0]
for i in range(c):
    for i in range(61**8):
        l[0] += 1
        for j in range(len(l)):
            if(l[j] == 62):
                l[j] = 0
                if(j+1 == len(l)):
                    l.append(0)
                else:
                    l[j+1] += 1
        s = []
        for i in range(len(l)):
            if(l[i] >= 0 and l[i] <= 9):
                s.append(chr(l[i]+48))
            elif(l[i] > 9 and l[i] <= 35):
                s.append(chr(l[i]+55))
            elif(l[i] > 35 and l[i] <= 62):
                s.append(chr(l[i]+61))
        print(s)