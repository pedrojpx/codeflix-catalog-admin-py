from uuid import UUID

import pytest

from src.core.category.application.create_category import create_category, InvalidCategoryData

class TestCreateCategory:
    def test_create_w_valid_data(self):
        c_id = create_category(name="Filme", description="Categoria para filmes", is_active=True)

        assert c_id is not None
        assert isinstance(c_id, UUID)
    
    def test_create_w_invalid_data(self):
        with pytest.raises(InvalidCategoryData, match="name cannot be empty") as exception_info:
            c_id = create_category(name="")

        assert exception_info.type is InvalidCategoryData
        
        with pytest.raises(InvalidCategoryData, match="name cannot be longer than 255 characters") as exception_info:
            c_id = create_category(name="a"*256)

        assert exception_info.type is InvalidCategoryData
