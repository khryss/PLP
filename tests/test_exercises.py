'''Test exercises'''


import unittest
import mock
import os
from PLP.exercises import e1_flatten, e2_merge_objects, e3_sort_dictionaries


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


class TestSortDictionaries(unittest.TestCase):
    '''Test sort dictionaries'''
    def test_lt(self):
        '''Test Dict.__lt__ method'''
        # given_expected = list(tuple(given_operand, given_operand, expected_result))
        given_expected = [(e3_sort_dictionaries.Dict({'a':0, 'b':2}),
                           e3_sort_dictionaries.Dict({'a':1, 'b':2}),
                           True),

                          (e3_sort_dictionaries.Dict({'bzz':2, 'azz':1}),
                           e3_sort_dictionaries.Dict({'czz':0, 'bzz':2}),
                           True),

                          (e3_sort_dictionaries.Dict({'a':0, 'b':1, 'c':0}),
                           e3_sort_dictionaries.Dict({'a':0, 'b':1, 'c':1}),
                           True),

                          (e3_sort_dictionaries.Dict({}),
                           e3_sort_dictionaries.Dict({'a':0, 'b':2}),
                           True),

                          (e3_sort_dictionaries.Dict({'a':1, 'b':2}),
                           e3_sort_dictionaries.Dict({'a':1, 'b':2}),
                           False)]

        for test_values in given_expected:
            self.assertEqual(test_values[0] < test_values[1], test_values[2])

    def test_gt(self):
        '''Test Dict.__lt__ method'''
        # given_expected = list(tuple(given_operand, given_operand, expected_result))
        given_expected = [(e3_sort_dictionaries.Dict({'a':1, 'b':2}),
                           e3_sort_dictionaries.Dict({'a':0, 'b':2}),
                           True),

                          (e3_sort_dictionaries.Dict({'bzz':0, 'azz':2}),
                           e3_sort_dictionaries.Dict({'czz':2, 'bzz':1}),
                           True),

                          (e3_sort_dictionaries.Dict({'a':0, 'b':1, 'c':1}),
                           e3_sort_dictionaries.Dict({'a':0, 'b':1, 'c':0}),
                           True),

                          (e3_sort_dictionaries.Dict({'a':0, 'b':2}),
                           e3_sort_dictionaries.Dict({}),
                           True),

                          (e3_sort_dictionaries.Dict({'a':1, 'b':2}),
                           e3_sort_dictionaries.Dict({'a':1, 'b':2}),
                           False)]

        for test_values in given_expected:
            self.assertEqual(test_values[0] > test_values[1], test_values[2])

    def test_quick_sort(self):
        '''Test _quick_sort function'''
        first_dict = e3_sort_dictionaries.Dict({'a':1, 'b':2})
        second_dict = e3_sort_dictionaries.Dict({'a':3})
        third_dict = e3_sort_dictionaries.Dict({'b':0})

        # given_expected = list(tuple(given_list, expected_result))
        given_expected = [([3, 5, 2, 6, 7, 2, 1, 9, 4, 8],
                           [1, 2, 2, 3, 4, 5, 6, 7, 8, 9]),

                          ([first_dict, second_dict, third_dict],
                           [third_dict, first_dict, second_dict]),

                          ([(3, 0), (0, 4), (1, 2)],
                           [(0, 4), (1, 2), (3, 0)])]

        for test_values in given_expected:
            self.assertEqual(e3_sort_dictionaries._quick_sort(test_values[0]),
                             test_values[1])

    @mock.patch('PLP.exercises.e3_sort_dictionaries._quick_sort')
    def test_order_dicts_from_file(self, mock_quick_sort):
        '''Tets order_dicts_from_file'''
        def _mock_quick_sort_side_effect(my_list):
            my_list.reverse()
            return my_list

        mock_quick_sort.side_effect = _mock_quick_sort_side_effect

        test_input_file = "test_order_dicts_input.txt"
        test_output_file = "test_order_dicts_output.txt"

        with open(test_input_file, "w") as in_file:
            in_file.write(
                "a 2  b 2 \n\n"
                "b 0  c 1 \n\n"
                "a 1     \n\n")

        e3_sort_dictionaries.order_dicts_from_file(test_input_file,
                                                   test_output_file)

        with open(test_output_file, "r") as out_file:
            output = out_file.readline()

        self.assertEqual(output, '(2, 1, 0)\n')

        os.remove(test_input_file)
        os.remove(test_output_file)


if __name__ == '__main__':
    unittest.main()
