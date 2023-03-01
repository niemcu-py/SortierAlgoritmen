import BubbleSort as bs
import QuickSort as qs
import datetime
import time
import random

#bslist = random.sample(range(0, 100), 100)
bslist = []
for i in range(1,5000):
    bslist.append(random.randint(-1000, 1000))
qslist = bslist.copy()

print(qslist)

startbs = datetime.datetime.now()
bslist = bs.bubblesort(bslist)
endbs = datetime.datetime.now()

startqs = datetime.datetime.now()
qslist = qs.quicksort(qslist)
endqs = datetime.datetime.now()

print('Die sortierte Liste nach BubbleSort')
print(str(bslist))
timebs = endbs - startbs
print('Die sortierte Liste nach QuickSort')
print(str(qslist))
timeqs = endqs - startqs
print('BubbleSort dauert:' + str(timebs))
print('QuickSort dauert:' + str(timeqs))
if timebs > timeqs:
    winner = 'QuickSort'
    timediff = timebs - timeqs
else:
    winner = 'BubbleSort'
    timediff = timeqs -timebs
print('damit ist' + winner + str(timediff) + 'schneller')