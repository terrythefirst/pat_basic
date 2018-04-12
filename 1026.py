CLK_TCK = 100
input_string = input()
timeSpan = int(input_string.split(' ')[1]) - int(input_string.split(' ')[0])
seconds = timeSpan//CLK_TCK
if timeSpan%100 >= 50:
    seconds += 1
hour = int(seconds//3600)
minute = int((seconds % 3600) // 60)
second = int(seconds % 60)
print("{0:02d}:{1:02d}:{2:02d}".format(hour, minute, second))
