def bubblesort(Olist):
    changed = True
    while(changed):
        changed = False
        for i in range(0, len(Olist) - 1):
            if not(i == (len(Olist) - 1)):
                if Olist[i] > Olist[i+1]:
                    j = Olist[i]
                    Olist[i] = Olist[i+1]
                    Olist[i+1] = j
                    changed = True

    return(Olist)