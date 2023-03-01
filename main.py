import datetime
import time
import random
import BubbleSort as bs
import QuickSort as qs

#bs_list = random.sample(range(0, 100), 100)
bs_list = []
for i in range(1,5000):
    bs_list.append(random.randint(-1000, 1000))
qs_list = bs_list.copy()

print(qs_list)

bs_start = datetime.datetime.now()
bs_list = bs.bubblesort(bs_list)
bs_end = datetime.datetime.now()

qs_start = datetime.datetime.now()
qs_list = qs.quicksort(qs_list)
qs_end = datetime.datetime.now()

print('Die sortierte Liste nach BubbleSort')
print(str(bs_list))
bs_time = bs_end - bs_start
print('Die sortierte Liste nach QuickSort')
print(str(qs_list))
qs_time = qs_end - qs_start
print('BubbleSort dauert:' + str(bs_time))
print('QuickSort dauert:' + str(qs_time))
if bs_time > qs_time:
    Winner = 'QuickSort'
    time_diff = bs_time - qs_time
else:
    Winner = 'BubbleSort'
    time_diff = qs_time -bs_time
print('damit ist' + Winner + str(time_diff) + 'schneller')