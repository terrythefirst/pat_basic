mean_to = input()
enter = input()
miss_set = set()
miss_list = []
for i in range(len(mean_to)):
    if enter.find(mean_to[i]) == -1:
        size = len(miss_set)
        miss_set.add(mean_to[i].upper())
        if size != len(miss_set):
            miss_list.append(mean_to[i].upper())
for i in miss_list:
    print(i, end='')

