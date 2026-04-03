from project.gallery import Gallery
import unittest


class TestGallery(unittest.TestCase):
    def setUp(self):
        self.gallery = Gallery("Gallery123", "Sofia", 150.5)

    def test_init_with_valid_data(self):
        self.assertEqual("Gallery123", self.gallery.gallery_name)
        self.assertEqual("Sofia", self.gallery.city)
        self.assertEqual(150.5, self.gallery.area_sq_m)
        self.assertTrue(self.gallery.open_to_public)
        self.assertEqual({}, self.gallery.exhibitions)

    def test_gallery_name_setter_strips_whitespace(self):
        gallery = Gallery("  Art2024  ", "Plovdiv", 90)
        self.assertEqual("Art2024", gallery.gallery_name)

    def test_gallery_name_raises_when_contains_invalid_characters(self):
        with self.assertRaises(ValueError) as exc:
            Gallery("Art Gallery", "Varna", 100)
        self.assertEqual("Gallery name can contain letters and digits only!", str(exc.exception))

    def test_city_raises_when_empty(self):
        with self.assertRaises(ValueError) as exc:
            Gallery("Art2024", "", 100)
        self.assertEqual("City name must start with a letter!", str(exc.exception))

    def test_city_raises_when_not_starting_with_letter(self):
        with self.assertRaises(ValueError) as exc:
            Gallery("Art2024", "1Sofia", 100)
        self.assertEqual("City name must start with a letter!", str(exc.exception))

    def test_area_sq_m_raises_when_zero_or_negative(self):
        with self.assertRaises(ValueError) as exc_zero:
            Gallery("Art2024", "Sofia", 0)
        self.assertEqual("Gallery area must be a positive number!", str(exc_zero.exception))

        with self.assertRaises(ValueError) as exc_negative:
            Gallery("Art2024", "Sofia", -5)
        self.assertEqual("Gallery area must be a positive number!", str(exc_negative.exception))

    def test_add_exhibition_successfully(self):
        result = self.gallery.add_exhibition("ModernArt", 2025)

        self.assertEqual('Exhibition "ModernArt" added for the year 2025.', result)
        self.assertEqual({"ModernArt": 2025}, self.gallery.exhibitions)

    def test_add_exhibition_when_already_exists(self):
        self.gallery.add_exhibition("ModernArt", 2025)

        result = self.gallery.add_exhibition("ModernArt", 2026)

        self.assertEqual('Exhibition "ModernArt" already exists.', result)
        self.assertEqual({"ModernArt": 2025}, self.gallery.exhibitions)

    def test_remove_exhibition_successfully(self):
        self.gallery.add_exhibition("ModernArt", 2025)

        result = self.gallery.remove_exhibition("ModernArt")

        self.assertEqual('Exhibition "ModernArt" removed.', result)
        self.assertEqual({}, self.gallery.exhibitions)

    def test_remove_exhibition_when_missing(self):
        result = self.gallery.remove_exhibition("MissingExpo")

        self.assertEqual('Exhibition "MissingExpo" not found.', result)
        self.assertEqual({}, self.gallery.exhibitions)

    def test_list_exhibitions_when_open_to_public(self):
        self.gallery.add_exhibition("ModernArt", 2025)
        self.gallery.add_exhibition("ClassicArt", 2024)

        result = self.gallery.list_exhibitions()

        self.assertEqual("ModernArt: 2025\nClassicArt: 2024", result)

    def test_list_exhibitions_when_closed_for_public(self):
        gallery = Gallery("Art2024", "Sofia", 120, False)
        gallery.add_exhibition("ModernArt", 2025)

        result = gallery.list_exhibitions()

        self.assertEqual(
            "Gallery Art2024 is currently closed for public! Check for updates later on.",
            result,
        )


if __name__ == "__main__":
    unittest.main()