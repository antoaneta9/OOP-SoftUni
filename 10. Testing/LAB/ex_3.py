import unittest


class IntegerListTests(unittest.TestCase):
    def setUp(self):
        self.integer_list = IntegerList(1, 2, 3, "a", 5.5)

    def test_constructor_takes_only_integers(self):
        self.assertEqual([1, 2, 3], self.integer_list.get_data())

    def test_add_method_adds_integer_and_returns_list(self):
        result = self.integer_list.add(10)
        self.assertEqual([1, 2, 3, 10], result)

    def test_add_method_raises_value_error_if_element_is_not_integer(self):
        with self.assertRaises(ValueError) as ex:
            self.integer_list.add("test")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_remove_index_returns_removed_element(self):
        result = self.integer_list.remove_index(1)
        self.assertEqual(2, result)

    def test_remove_index_raises_index_error_if_index_is_out_of_range(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.remove_index(10)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_returns_element_at_index(self):
        result = self.integer_list.get(0)
        self.assertEqual(1, result)

    def test_get_raises_index_error_if_index_is_out_of_range(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.get(10)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_adds_element_at_correct_index(self):
        self.integer_list.insert(1, 10)
        self.assertEqual([1, 10, 2, 3], self.integer_list.get_data())

    def test_insert_raises_index_error_if_index_is_out_of_range(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.insert(10, 10)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_raises_value_error_if_element_is_not_integer(self):
        with self.assertRaises(ValueError) as ex:
            self.integer_list.insert(1, "test")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_get_biggest_returns_biggest_element(self):
        result = self.integer_list.get_biggest()
        self.assertEqual(3, result)

    def test_get_index_returns_index_of_element(self):
        result = self.integer_list.get_index(2)
        self.assertEqual(1, result)


if __name__ == "__main__":
    unittest.main()