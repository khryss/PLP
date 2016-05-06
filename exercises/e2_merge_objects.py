'''Merge objects'''


def merge_objects(object1, object2):
    '''Merge two objects with any depth'''
    result = {}
    for key1 in object1.keys():
        value1 = object1[key1]
        value2 = object2.get(key1)
        if not value2:
            # the key is in first object and not in the second
            result[key1] = value1
        elif type(value1) != type(value2):
            # type mismatch between the objects pair
            result[key1] = (value1, value2)
        elif isinstance(value1, dict):
            # this pair of objects should be also merged
            result[key1] = merge_objects(value1, value2)
        elif isinstance(value1, set):
            # to merge two sets use union instead of '+'
            result[key1] = value1.union(value2)
        else:
            result[key1] = value1 + value2

    for key2 in list(set(object2.keys()) - set(object1.keys())):
        # append all the objects left in object2
        result[key2] = object2[key2]
    return result
