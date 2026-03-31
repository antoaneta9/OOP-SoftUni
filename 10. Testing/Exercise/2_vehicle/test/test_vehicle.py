import unittest

from project.vehicle import Vehicle


class VehicleTests(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle(100, 200)

    def test_init(self):
        self.assertEqual(100, self.vehicle.fuel)
        self.assertEqual(100, self.vehicle.capacity)
        self.assertEqual(200, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_default_fuel_consumption(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_raises_exception_when_not_enough_fuel(self):
        vehicle = Vehicle(1, 100)
        with self.assertRaises(Exception) as ex:
            vehicle.drive(1)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_reduces_fuel_when_enough_fuel(self):
        self.vehicle.drive(10)
        self.assertEqual(87.5, self.vehicle.fuel)

    def test_refuel_raises_exception_when_too_much_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_adds_fuel_correctly(self):
        vehicle = Vehicle(50, 150)
        vehicle.fuel = 30
        vehicle.refuel(20)
        self.assertEqual(50, vehicle.fuel)

    def test_str_returns_correct_result(self):
        expected = "The vehicle has 200 horse power with 100 fuel left and 1.25 fuel consumption"
        self.assertEqual(expected, str(self.vehicle))


if __name__ == "__main__":
    unittest.main()