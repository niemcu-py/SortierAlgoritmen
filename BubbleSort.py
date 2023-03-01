def bubblesort(list):
    changed = True
    while(changed):
        changed = False
        for i in range(0, len(list) - 1):
            if not(i == (len(list) - 1)):
                if list[i] > list[i+1]:
                    j = list[i]
                    list[i] = list[i+1]
                    list[i+1] = j
                    changed = True

    return(list)