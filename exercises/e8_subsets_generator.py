'''Subsets generator of a given set'''


from itertools import combinations


def subsets(my_set):
    for i in range(len(my_set)+1):
        for comb in combinations(my_set, i):
            yield set(comb)
