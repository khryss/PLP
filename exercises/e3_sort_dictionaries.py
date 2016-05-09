'''Sort dictionaries from a file'''


import sys
from itertools import izip


class Dict(dict):
    '''
    Dict compare operators definition.

    A Dict is smaller if the value of the smallest key is smaller then
    the value of the smallest key of the other Dict. If these are equal,
    compare the second smallest pair of keys and so on.

    '''

    def __init__(self, my_dict):
        super(Dict, self).__init__(my_dict)
        self._dict = my_dict

    def __lt__(self, arg):
        my_sorted_items = sorted(self._dict.items())
        arg_sorted_items = sorted(arg.items())

        for my_item, arg_item in zip(my_sorted_items, arg_sorted_items):
            if my_item[1] < arg_item[1]:
                return True
            elif my_item[1] > arg_item[1]:
                return False
        if len(my_sorted_items) < len(arg_sorted_items):
            return True
        return False

    def __gt__(self, arg):
        my_sorted_items = sorted(self._dict.items())
        arg_sorted_items = sorted(arg.items())

        for my_item, arg_item in zip(my_sorted_items, arg_sorted_items):
            if my_item[1] > arg_item[1]:
                return True
            elif my_item[1] < arg_item[1]:
                return False
        if len(my_sorted_items) > len(arg_sorted_items):
            return True
        return False


def _quick_sort(my_list):
    if len(my_list) <= 1:
        return my_list
    pivot = my_list[0]
    check_idx = 0

    for i in range(1, len(my_list)):
        if my_list[i] < pivot:
            check_idx += 1
            my_list[i], my_list[check_idx] = my_list[check_idx], my_list[i]

    my_list[0], my_list[check_idx] = my_list[check_idx], my_list[0]

    my_list[:check_idx] = _quick_sort(my_list[:check_idx])
    my_list[check_idx+1:] = _quick_sort(my_list[check_idx+1:])

    return my_list


def order_dicts_from_file(my_input_file, my_output_file):
    '''
    Writes in my_output_file arg the order of dicts

    '''
    dict_list = []
    line_dict_order_idx = 0

    with open(my_input_file, "r") as my_file:
        for line in my_file.readlines():
            if not line.strip():
                continue
            it_line = iter(line.split())
            my_dict = Dict(dict(izip(it_line, it_line)))

            # To keep track of the file dict order info,
            # it is saved in a tuple with the dict itself
            dict_list.append((my_dict, line_dict_order_idx))
            line_dict_order_idx += 1

    with open(my_output_file, "w") as my_file:
        # Get the order info out of the dict
        dict_order = zip(*_quick_sort(dict_list))[1]
        my_file.write(str(dict_order) + "\n")


if __name__ == "__main__":
    order_dicts_from_file(*sys.argv[1:])
