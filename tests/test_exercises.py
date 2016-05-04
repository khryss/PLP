'''Test exercises'''


import unittest
from PLP.exercises import e1_flatten


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


if __name__ == '__main__':
    unittest.main()
