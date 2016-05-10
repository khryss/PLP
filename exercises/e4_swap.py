'''Swap keys with values in a dict'''


import collections


def _is_hashable(obj):
    if not isinstance(obj, collections.Hashable):
        return False
    if isinstance(obj, collections.Iterable):
        for i in obj:
            if not i is obj:
                if not _is_hashable(i):
                    return False
    return True


def swap(my_dict):
    '''Swaps keys with values of my_dict and returns it'''
    for item in my_dict.items():
        if not _is_hashable(item[1]):
            raise Exception("Swap is imposible! " + str(item[1]) + " "
                            "can not be used as a key!")
        else:
            my_dict[item[1]] = item[0]
            del my_dict[item[0]]
    return my_dict
