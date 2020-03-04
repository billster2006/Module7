import unittest
from unittest.mock import patch
import fun_with_collections.basic_list_exception as topic1


@patch('fun_with_collections.topic1.get_input', return_value='ab')  # patch function for input
def test_make_list_non_numeric(self):  # pass input
    with self.assertRaises(ValueError):  # this is familiar
        topic1.make_list()  # call the function!

if __name__ == '__main__':
    unittest.main()