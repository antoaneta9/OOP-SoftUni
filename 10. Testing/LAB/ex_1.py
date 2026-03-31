import unittest


class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("Ivan", 1000, 10)

    def test_worker_is_initialized_correctly(self):
        self.assertEqual("Ivan", self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(10, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_rest_increases_energy(self):
        self.worker.rest()
        self.assertEqual(11, self.worker.energy)

    def test_work_raises_error_when_energy_is_zero(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_work_raises_error_when_energy_is_negative(self):
        self.worker.energy = -1
        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_work_increases_money_correctly(self):
        self.worker.work()
        self.assertEqual(1000, self.worker.money)

    def test_work_decreases_energy(self):
        self.worker.work()
        self.assertEqual(9, self.worker.energy)

    def test_get_info_returns_correct_string(self):
        self.assertEqual("Ivan has saved 0 money.", self.worker.get_info())


if __name__ == "__main__":
    unittest.main()