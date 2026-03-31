from project.furniture import Furniture
import unittest

class TestFurniture(unittest.TestCase):
    def setUp(self):
        self.furniture = Furniture("Chair", 120.50, (100, 50, 60), True, 7.5)

    def test_init_with_all_valid_data(self):
        furniture = Furniture("Table", 250.00, (120, 80, 75), False, 15.2)

        self.assertEqual("Table", furniture.model)
        self.assertEqual(250.00, furniture.price)
        self.assertEqual((120, 80, 75), furniture.dimensions)
        self.assertFalse(furniture.in_stock)
        self.assertEqual(15.2, furniture.weight)

    def test_init_with_default_values(self):
        furniture = Furniture("Desk", 300.00, (150, 70, 80))

        self.assertEqual("Desk", furniture.model)
        self.assertEqual(300.00, furniture.price)
        self.assertEqual((150, 70, 80), furniture.dimensions)
        self.assertTrue(furniture.in_stock)
        self.assertIsNone(furniture.weight)

    def test_model_setter_valid_value(self):
        self.furniture.model = "Sofa"
        self.assertEqual("Sofa", self.furniture.model)

    def test_model_setter_raises_when_empty_string(self):
        with self.assertRaises(ValueError) as ex:
            self.furniture.model = ""

        self.assertEqual(
            "Model must be a non-empty string with a maximum length of 50 characters.",
            str(ex.exception)
        )

    def test_model_setter_raises_when_whitespace_only(self):
        with self.assertRaises(ValueError) as ex:
            self.furniture.model = "   "

        self.assertEqual(
            "Model must be a non-empty string with a maximum length of 50 characters.",
            str(ex.exception)
        )

    def test_model_setter_raises_when_length_above_50(self):
        with self.assertRaises(ValueError) as ex:
            self.furniture.model = "a" * 51

        self.assertEqual(
            "Model must be a non-empty string with a maximum length of 50 characters.",
            str(ex.exception)
        )

    def test_model_setter_accepts_length_50(self):
        model = "a" * 50
        self.furniture.model = model
        self.assertEqual(model, self.furniture.model)

    def test_price_setter_valid_zero(self):
        self.furniture.price = 0.0
        self.assertEqual(0.0, self.furniture.price)

    def test_price_setter_valid_positive_value(self):
        self.furniture.price = 999.99
        self.assertEqual(999.99, self.furniture.price)

    def test_price_setter_raises_when_negative(self):
        with self.assertRaises(ValueError) as ex:
            self.furniture.price = -0.01

        self.assertEqual(
            "Price must be a non-negative number.",
            str(ex.exception)
        )

    def test_dimensions_setter_valid_value(self):
        self.furniture.dimensions = (200, 100, 50)
        self.assertEqual((200, 100, 50), self.furniture.dimensions)

    def test_dimensions_setter_raises_when_tuple_length_not_3(self):
        with self.assertRaises(ValueError) as ex:
            self.furniture.dimensions = (100, 50)

        self.assertEqual(
            "Dimensions tuple must contain 3 integers.",
            str(ex.exception)
        )

    def test_dimensions_setter_raises_when_some_dimension_is_zero(self):
        with self.assertRaises(ValueError) as ex:
            self.furniture.dimensions = (100, 0, 50)

        self.assertEqual(
            "Dimensions tuple must contain integers greater than zero.",
            str(ex.exception)
        )

    def test_dimensions_setter_raises_when_some_dimension_is_negative(self):
        with self.assertRaises(ValueError) as ex:
            self.furniture.dimensions = (100, -5, 50)

        self.assertEqual(
            "Dimensions tuple must contain integers greater than zero.",
            str(ex.exception)
        )

    def test_weight_setter_valid_positive_value(self):
        self.furniture.weight = 12.3
        self.assertEqual(12.3, self.furniture.weight)

    def test_weight_setter_valid_none(self):
        self.furniture.weight = None
        self.assertIsNone(self.furniture.weight)

    def test_weight_setter_raises_when_zero(self):
        with self.assertRaises(ValueError) as ex:
            self.furniture.weight = 0.0

        self.assertEqual(
            "Weight must be greater than zero.",
            str(ex.exception)
        )

    def test_weight_setter_raises_when_negative(self):
        with self.assertRaises(ValueError) as ex:
            self.furniture.weight = -2.5

        self.assertEqual(
            "Weight must be greater than zero.",
            str(ex.exception)
        )

    def test_get_available_status_when_in_stock_is_true(self):
        furniture = Furniture("Wardrobe", 400.00, (200, 100, 60), True, 45.0)

        result = furniture.get_available_status()

        self.assertEqual(
            "Model: Wardrobe is currently in stock.",
            result
        )

    def test_get_available_status_when_in_stock_is_false(self):
        furniture = Furniture("Wardrobe", 400.00, (200, 100, 60), False, 45.0)

        result = furniture.get_available_status()

        self.assertEqual(
            "Model: Wardrobe is currently unavailable.",
            result
        )

    def test_get_specifications_with_weight(self):
        furniture = Furniture("Shelf", 150.00, (180, 80, 30), True, 20.5)

        result = furniture.get_specifications()

        self.assertEqual(
            "Model: Shelf has the following dimensions: 180mm x 80mm x 30mm and weighs: 20.5",
            result
        )

    def test_get_specifications_without_weight(self):
        furniture = Furniture("Shelf", 150.00, (180, 80, 30), True, None)

        result = furniture.get_specifications()

        self.assertEqual(
            "Model: Shelf has the following dimensions: 180mm x 80mm x 30mm and weighs: N/A",
            result
        )


if __name__ == "__main__":
    unittest.main()