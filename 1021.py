ss = input()
array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for c in range(len(ss)):
    array[int(ss[c])-int('0')] += 1
for i in range(10):
    if array[i] != 0:
        print(i, end='')
        print(":", end='')
        print(array[i])