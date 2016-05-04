'''Implement a function that will flatten
two lists up to a maximum given depth.'''


def flatten(my_list1, my_list2, depth=1):
    '''Flatten two lists up to a given depth'''
    return (_flatten_list(my_list1, depth), _flatten_list(my_list2, depth))


def _flatten_list(my_list, depth=1):
    if not depth:
        return my_list
    temp = []
    for element in my_list:
        if isinstance(element, (list, tuple)):
            temp.extend(_flatten_list(element, depth-1))
        else:
            temp.append(element)
    return temp
