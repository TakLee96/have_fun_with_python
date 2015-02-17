__author__ = 'lijiahang'

def remove_all(el, lst):
    # while el in lst:
    #     lst.remove(el)
    for x in lst:
        if x == el:
            lst.remove(el)

def square_elements(lst):
    for index in range(len(lst)):
        lst[index] = lst[index] * lst[index]