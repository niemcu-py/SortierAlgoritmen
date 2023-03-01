def quicksort(Olist):
    if len(Olist) % 2 == 0:
        pivot = Olist[int(len(Olist)/2)]
    else:
        pivot = Olist[int((len(Olist)-1)/2)]
    
    Slist = []
    Llist = []
    Mlist = []

    for i in Olist:
        if i < pivot:
            Slist.append(i)
        elif i > pivot:
            Llist.append(i)
        else:
            Mlist.append(i)
    
    if len(Slist) > 1:
        Slist = quicksort(Slist)
    if len(Llist) > 1:
        Llist = quicksort(Llist)

    rlist = Slist + Mlist + Llist

    return(rlist)