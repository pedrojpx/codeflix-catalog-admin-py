import pytest

from category import Category
import uuid

class TestCategory():
    def test_name_is_required(self):
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'name'"):
            Category()

    def test_name_must_have_less_than_255_characters(self):
        with pytest.raises(ValueError, match="name cannot be longer than 255 characters"):
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

    def test_cannot_create_category_with_empty_name(self):
        with pytest.raises(ValueError, match="name cannot be empty"):
            c = Category(name="")

class TestUpdateCategory:
    def test_update_category_with_name_and_description(self):
        c = Category(name="Filme", description="Filmes em geral")

        c.update_category(name="doc", description="docs em geral")

        assert c.name == "doc"
        assert c.description == "docs em geral"
    
    def test_update_category_with_invalid_name(self):
        c = Category(name="Filme", description="Filmes em geral")

        with pytest.raises(ValueError, match="name cannot be longer than 255 characters"):
            c.update_category(name="a"*256, description="docs em geral")

    def test_cannot_update_category_with_empty_name(self):
        c = Category(name="Filme", description="Filmes em geral")

        with pytest.raises(ValueError, match="name cannot be empty"):
            c.update_category(name="", description="a")

class TestActivateCategory:
    def test_activate_category(self):
        c = Category(name="Filme", description="Filmes em geral", is_active=False)

        c.activate()

        assert c.is_active is True
    
    def test_activate_activated_category(self):
        c = Category(name="Filme", description="Filmes em geral")

        c.activate()

        assert c.is_active is True

    def test_deactivate_category(self):
        c = Category(name="Filme", description="Filmes em geral")

        c.deactivate()

        assert c.is_active is False

    def test_deactivate_deactivated_category(self):
        c = Category(name="Filme", description="Filmes em geral", is_active=False)

        c.deactivate()

        assert c.is_active is False
        
class TestEquality:
    def test_equality_through_id(self):
        common_id = uuid.uuid4()
        c1 = Category(id=common_id, name="Filme", description="Filmes em geral")
        c2 = Category(id=common_id, name="Filme", description="Filmes em geral")

        assert c1 == c2
        
    def test_equality_different_class(self):
        class Dummy:
            pass
        
        common_id = uuid.uuid4()
        c1 = Category(id=common_id, name="Filme", description="Filmes em geral")
        c2 = Dummy()
        c2.id = common_id

        assert c1 != c2

    