# -*- coding utf-8 -*-

string = input()
ss = []
flag = 1
for num in string.split():
    ss.append(int(num))
for i in range(1, 10):
    if ss[i] != 0:
        print(i, end='')
        ss[i] -= 1
        flag = 0
        break
if flag:
    print(0, end='')
else:
    for i in range(len(ss)):
        for j in range(ss[i]):
            print(i, end='')