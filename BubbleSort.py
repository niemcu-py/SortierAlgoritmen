def bubblesort(o_list):
    changed = True
    while changed:
        changed = False
        for i in range(0, len(o_list) - 1):
            if not i == (len(o_list) - 1):
                if o_list[i] > o_list[i+1]:
                    j = o_list[i]
                    o_list[i] = o_list[i+1]
                    o_list[i+1] = j
                    changed = True

    return o_list
