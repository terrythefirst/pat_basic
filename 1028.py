#GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
import time
n = int(input())
legal_count = 0
oldest = 10000
youngest = 0
oldest_name,youngest_name = "no","no"
while n > 0:
    n -= 1
    input_string = input()
    name = input_string.split(' ')[0]
    strtime = time.strptime(input_string.split(' ')[1], "%Y/%m/%d")
    print("strtime = {}".format(strtime))
    age = 0
    #age = time.mktime(time.strptime("2014/09/06", "%Y/%m/%d")) - time.mktime(strtime)
    #age = int(age / (3600 * 24 * 365))
    print("age = {0}".format(age))
    if (age >= 0) & (age <= 200):
        legal_count += 1
        if age >= oldest:
            oldest_name = name
        elif age <= youngest:
            youngest_name = name
print("{0} {1} {2}".format(legal_count, oldest_name, youngest_name))