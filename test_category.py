import unittest

from category import Category
from uuid import UUID

class TestCategory(unittest.TestCase):
    def test_name_is_required(self):
        with self.assertRaisesRegex(TypeError, "missing 1 required positional argument: 'name'"):
            Category()

    def test_name_must_have_less_than_255_characters(self):
        with self.assertRaisesRegex(TypeError, "name must have less than 256 characters"):
            Category(name="a"*256)

    def test_category_must_be_created_with_id_as_uuid(self):
        c = Category(name="filme")
        self.assertEqual(type(c.id), UUID)

    def test_category_active_by_default(self):
        c = Category(name="filme")
        self.assertEqual(c.is_active, True)

    def test_created_category_with_default_values(self):
        c = Category(name="filme")
        self.assertEqual(c.name, "filme")
        self.assertEqual(c.description, "")
        self.assertEqual(c.is_active, True)

    def test_created_category_with_provided_values(self):
        c = Category("filme", "id", "description", False)
        self.assertEqual(c.id, "id")
        self.assertEqual(c.name, "filme")
        self.assertEqual(c.description, "description")
        self.assertEqual(c.is_active, False)


if __name__ == "__main__":
    unittest.main()