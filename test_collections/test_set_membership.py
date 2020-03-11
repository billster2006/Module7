import unittest
from fun_with_collections import set_membership as membership

class MyTestCase(unittest.TestCase):
    def test_in_set_true(self):  # pass input
        my_set = {1, 2, 3, 4}
        self.assertEqual(membership.in_set(my_set),'Set is true')

    def test_in_set_false(self):
        my_set = {1,2,3,4}
        self.assertNotEqual(membership.in_set(my_set), 'Set is false')

if __name__ == '__main__':
    unittest.main()
