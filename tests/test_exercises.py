'''Test exercises'''


import unittest
from PLP.exercises import e1_flatten, e2_merge_objects


class TestFlatten(unittest.TestCase):
    '''Test flatten'''
    def test_flatten(self):
        '''Test flatten function'''
        given = [([[[1, 2], 3], 4],  [1, 2, [3]],  2),
                 (((1,), 2),         [1, 2, 3],    1),
                 ((((1,), 2), 3),    []             )]
        expected = [([1, 2, 3, 4],   [1, 2, 3]),
                    ([1, 2],         [1, 2, 3]),
                    ([(1,), 2, 3],   [])]
        for g, e in zip(given, expected):
            self.assertEqual(e1_flatten.flatten(*g), e)


class TestMergeObjects(unittest.TestCase):
    '''Test merge objects'''
    def test_merge_objets(self):
        '''Test merge_objects function'''
        given = (
            {'a':1, 'b':[1, 2, 3], 'c':set(['ab', 1]), 'd':100, 'e':10, 'g':{'h':'abc'}},
            {'a':2, 'b':[3, 2, 4], 'c':set(['bc', 1]), 'd':'a', 'f':20, 'g':{'h':'def'}})
        expected = {'a':3, 'b':[1, 2, 3, 3, 2, 4], 'c':set([1, 'ab', 'bc']), 'd':(100, 'a'),
                    'e':10, 'f':20, 'g':{'h':'abcdef'}}
        self.assertEqual(e2_merge_objects.merge_objects(*given), expected)

if __name__ == '__main__':
    unittest.main()
