import unittest
from project.climbing_robot import ClimbingRobot


class TestClimbingRobot(unittest.TestCase):
    def setUp(self):
        self.robot = ClimbingRobot("Mountain", "Arm", 100, 200)

    def test_init_valid(self):
        self.assertEqual("Mountain", self.robot.category)
        self.assertEqual("Arm", self.robot.part_type)
        self.assertEqual(100, self.robot.capacity)
        self.assertEqual(200, self.robot.memory)
        self.assertEqual([], self.robot.installed_software)

    def test_category_raises_when_invalid(self):
        with self.assertRaises(ValueError) as ex:
            ClimbingRobot("Sea", "Arm", 100, 200)
        self.assertEqual(
            "Category should be one of ['Mountain', 'Alpine', 'Indoor', 'Bouldering']",
            str(ex.exception)
        )

    def test_get_used_capacity_when_no_software(self):
        self.assertEqual(0, self.robot.get_used_capacity())

    def test_get_used_capacity_with_installed_software(self):
        self.robot.installed_software = [
            {"name": "Soft1", "capacity_consumption": 20, "memory_consumption": 30},
            {"name": "Soft2", "capacity_consumption": 15, "memory_consumption": 10},
        ]
        self.assertEqual(35, self.robot.get_used_capacity())

    def test_get_available_capacity(self):
        self.robot.installed_software = [
            {"name": "Soft1", "capacity_consumption": 40, "memory_consumption": 20}
        ]
        self.assertEqual(60, self.robot.get_available_capacity())

    def test_get_used_memory_when_no_software(self):
        self.assertEqual(0, self.robot.get_used_memory())

    def test_get_used_memory_with_installed_software(self):
        self.robot.installed_software = [
            {"name": "Soft1", "capacity_consumption": 20, "memory_consumption": 30},
            {"name": "Soft2", "capacity_consumption": 15, "memory_consumption": 10},
        ]
        self.assertEqual(40, self.robot.get_used_memory())

    def test_get_available_memory(self):
        self.robot.installed_software = [
            {"name": "Soft1", "capacity_consumption": 20, "memory_consumption": 80}
        ]
        self.assertEqual(120, self.robot.get_available_memory())

    def test_install_software_successfully(self):
        software = {"name": "ClimbOS", "capacity_consumption": 30, "memory_consumption": 50}

        result = self.robot.install_software(software)

        self.assertEqual(
            "Software 'ClimbOS' successfully installed on Mountain part.",
            result
        )
        self.assertEqual([software], self.robot.installed_software)

    def test_install_software_fails_when_not_enough_capacity(self):
        software = {"name": "ClimbOS", "capacity_consumption": 150, "memory_consumption": 50}

        result = self.robot.install_software(software)

        self.assertEqual(
            "Software 'ClimbOS' cannot be installed on Mountain part.",
            result
        )
        self.assertEqual([], self.robot.installed_software)

    def test_install_software_fails_when_not_enough_memory(self):
        software = {"name": "ClimbOS", "capacity_consumption": 30, "memory_consumption": 250}

        result = self.robot.install_software(software)

        self.assertEqual(
            "Software 'ClimbOS' cannot be installed on Mountain part.",
            result
        )
        self.assertEqual([], self.robot.installed_software)

    def test_install_software_success_with_exact_resources(self):
        software = {"name": "ClimbOS", "capacity_consumption": 100, "memory_consumption": 200}

        result = self.robot.install_software(software)

        self.assertEqual(
            "Software 'ClimbOS' successfully installed on Mountain part.",
            result
        )
        self.assertEqual([software], self.robot.installed_software)


if __name__ == "__main__":
    unittest.main()