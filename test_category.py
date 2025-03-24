import pytest

from category import Category
from uuid import UUID

class TestCategory():
    def test_name_is_required(self):
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'name'"):
            Category()

    def test_name_must_have_less_than_255_characters(self):
        with pytest.raises(TypeError, match="name must have less than 256 characters"):
            Category(name="a"*256)

    def test_category_must_be_created_with_id_as_uuid(self):
        c = Category(name="filme")
        assert isinstance(c.id, UUID)

    def test_category_active_by_default(self):
        c = Category(name="filme")
        assert c.is_active == True

    def test_created_category_with_default_values(self):
        c = Category(name="filme")
        assert c.name == "filme"
        assert c.description == ""
        assert c.is_active is True

    def test_created_category_with_provided_values(self):
        c = Category("filme", "id", "description", False)
        assert c.id == "id"
        assert c.name == "filme"
        assert c.description == "description"
        assert c.is_active is False