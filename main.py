import datetime
import time
import random
import BubbleSort as bs
import QuickSort as qs

#BSlist = random.sample(range(0, 100), 100)
BSlist = []
for i in range(1,5000):
    BSlist.append(random.randint(-1000, 1000))
QSlist = BSlist.copy()

print(QSlist)

BSstart = datetime.datetime.now()
BSlist = bs.bubblesort(BSlist)
BSend = datetime.datetime.now()

QSstart = datetime.datetime.now()
QSlist = qs.quicksort(QSlist)
QSend = datetime.datetime.now()

print('Die sortierte Liste nach BubbleSort')
print(str(BSlist))
BStime = BSend - BSstart
print('Die sortierte Liste nach QuickSort')
print(str(QSlist))
QStime = QSend - QSstart
print('BubbleSort dauert:' + str(BStime))
print('QuickSort dauert:' + str(QStime))
if BStime > QStime:
    Winner = 'QuickSort'
    TimeDiff = BStime - QStime
else:
    Winner = 'BubbleSort'
    TimeDiff = QStime -BStime
print('damit ist' + Winner + str(TimeDiff) + 'schneller')