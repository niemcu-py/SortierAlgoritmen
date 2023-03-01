def quicksort(list):
    if len(list) % 2 == 0:
        pivot = list[int(len(list)/2)]
    else:
        pivot = list[int((len(list)-1)/2)]
    
    slist = []
    llist = []
    mlist = []

    for i in list:
        if i < pivot:
            slist.append(i)
        elif i > pivot:
            llist.append(i)
        else:
            mlist.append(i)
    
    if len(slist) > 1:
        slist = quicksort(slist)
    if len(llist) > 1:
        llist = quicksort(llist)

    rlist = slist + mlist + llist

    return(rlist)