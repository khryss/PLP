'''Tree iterator in pre-order'''

def tree_iter(tree):
    # tree format: ('a', ('b', None, None), None)
    if tree:
        name, child_left, child_right = tree
        yield name
        for left in tree_iter(child_left):
            yield left
        for right in tree_iter(child_right):
            yield right
