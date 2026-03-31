import unittest

from project.mammal import Mammal


class MammalTests(unittest.TestCase):
    def setUp(self):
        self.mammal = Mammal("Dog", "Canine", "Bark")

    def test_init(self):
        self.assertEqual("Dog", self.mammal.name)
        self.assertEqual("Canine", self.mammal.type)
        self.assertEqual("Bark", self.mammal.sound)
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_make_sound_returns_correct_result(self):
        self.assertEqual("Dog makes Bark", self.mammal.make_sound())

    def test_get_kingdom_returns_correct_result(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info_returns_correct_result(self):
        self.assertEqual("Dog is of type Canine", self.mammal.info())


if __name__ == "__main__":
    unittest.main()