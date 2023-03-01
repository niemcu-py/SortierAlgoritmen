"""This module contains a quicksort algorithm"""

def quicksort(o_list):
    """the implementation of the quick sort algorithm"""
    if o_list == []:
        return []

    if len(o_list) % 2 == 0:
        pivot = o_list[int(len(o_list)/2)]
    else:
        pivot = o_list[int((len(o_list)-1)/2)]

    s_list = []
    l_list = []
    m_list = []

    for i in o_list:
        if i < pivot:
            s_list.append(i)
        elif i > pivot:
            l_list.append(i)
        else:
            m_list.append(i)

    if len(s_list) > 1:
        s_list = quicksort(s_list)
    if len(l_list) > 1:
        l_list = quicksort(l_list)

    rlist = s_list + m_list + l_list

    return rlist
