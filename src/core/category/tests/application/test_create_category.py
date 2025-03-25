from unittest.mock import MagicMock
from uuid import UUID

import pytest

from src.core.category.infra.in_memory_category import InMemoryCategoryRepository
from src.core.category.application.create_category import create_category, InvalidCategoryData

class TestCreateCategory:
    def test_create_w_valid_data(self):
        mock_repo = MagicMock(InMemoryCategoryRepository)
        c_id = create_category(repository=mock_repo, name="Filme", description="Categoria para filmes", is_active=True)

        assert c_id is not None
        assert isinstance(c_id, UUID)
        assert mock_repo.save.called
    
    def test_create_w_invalid_data(self):
        mock_repo = MagicMock(InMemoryCategoryRepository)
        with pytest.raises(InvalidCategoryData, match="name cannot be empty") as exception_info:
            c_id = create_category(repository=mock_repo, name="")

        assert exception_info.type is InvalidCategoryData
        
        with pytest.raises(InvalidCategoryData, match="name cannot be longer than 255 characters") as exception_info:
            c_id = create_category(repository=mock_repo, name="a"*256)

        assert exception_info.type is InvalidCategoryData
