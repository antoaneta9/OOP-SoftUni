import unittest


class CarTests(unittest.TestCase):
    def setUp(self):
        self.car = Car("BMW", "X5", 10, 20)

    def test_constructor_initializes_correctly(self):
        self.assertEqual("BMW", self.car.make)
        self.assertEqual("X5", self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(0, self.car.fuel_amount)
        self.assertEqual(20, self.car.fuel_capacity)

    def test_make_raises_exception_when_empty(self):
        with self.assertRaises(Exception) as ex:
            Car("", "X5", 10, 20)
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_raises_exception_when_empty(self):
        with self.assertRaises(Exception) as ex:
            Car("BMW", "", 10, 20)
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_raises_exception_when_zero_or_negative(self):
        with self.assertRaises(Exception) as ex:
            Car("BMW", "X5", 0, 20)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_raises_exception_when_zero_or_negative(self):
        with self.assertRaises(Exception) as ex:
            Car("BMW", "X5", 10, 0)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_raises_exception_when_negative(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_raises_exception_when_amount_is_zero_or_negative(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_adds_fuel_correctly(self):
        self.car.refuel(10)
        self.assertEqual(10, self.car.fuel_amount)

    def test_refuel_does_not_exceed_capacity(self):
        self.car.refuel(50)
        self.assertEqual(20, self.car.fuel_amount)

    def test_drive_raises_exception_when_not_enough_fuel(self):
        self.car.fuel_amount = 5
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_reduces_fuel_correctly(self):
        self.car.fuel_amount = 20
        self.car.drive(100)
        self.assertEqual(10, self.car.fuel_amount)


if __name__ == "__main__":
    unittest.main()