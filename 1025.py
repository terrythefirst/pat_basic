#It's not faster enough to AC it
class ListNode:
    def __init__(self, add, data, next_add):
        self.data = data
        self.nextAdd = next_add
        self.add = add

string = input()
firstAdd = string.split(" ")[0]
totalCount = int(string.split(" ")[1])
constK = int(string.split(" ")[2])
ListNodeDict = {}
while totalCount > 0:
    ss = input()
    tt = ss.split(' ')
    ListNodeDict[tt[0]] = ListNode(tt[0], tt[1], tt[2])
    totalCount -= 1

j = firstAdd
stack = []
count = 0
fistReverse = 1
while (j != '-1') & (constK > 1) & (len(ListNodeDict) >= constK):
    count += 1
    ln = ListNodeDict[j]
    j = ln.nextAdd
    stack.append(ln)
    if count == constK:
        cutHead = stack.pop()
        if fistReverse == 1:
            firstAdd = cutHead.add
            fistReverse = 0
        else:
            preCutLast.nextAdd = cutHead.add

        pre = cutHead
        while len(stack) != 0:
            next = stack.pop()
            pre.nextAdd = next.add
            pre = next
        next.nextAdd = j
        count = 0
        preCutLast = next

i = firstAdd
while i != '-1':
    ln = ListNodeDict[i]
    print(i+' '+ln.data+' '+ln.nextAdd)
    i = ln.nextAdd
if firstAdd == '-1':
    print('-1')