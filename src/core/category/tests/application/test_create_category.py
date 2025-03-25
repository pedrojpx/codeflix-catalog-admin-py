from unittest.mock import MagicMock
from uuid import UUID

import pytest

from src.core.category.infra.in_memory_category import InMemoryCategoryRepository
from src.core.category.application.create_category import CreateCategoryRequest, CreateCategoryUseCase, InvalidCategoryData
from src.core.category.application.exceptions import InvalidCategoryData

class TestCreateCategory:
    def test_create_w_valid_data(self):
        mock_repo = MagicMock(InMemoryCategoryRepository)
        use_case = CreateCategoryUseCase(mock_repo)
        request = CreateCategoryRequest(
            name="Filme", 
            description="Categoria para filmes", 
            is_active=True
        )

        c_id = use_case.execute(request)

        assert c_id is not None
        assert isinstance(c_id, UUID)
        assert mock_repo.save.called
    
    def test_create_w_invalid_data(self):
        mock_repo = MagicMock(InMemoryCategoryRepository)
        use_case = CreateCategoryUseCase(mock_repo)
        request = CreateCategoryRequest(
            name="", 
            description="Categoria para filmes", 
            is_active=True
        )

        with pytest.raises(InvalidCategoryData, match="name cannot be empty") as exception_info:
            c_id = use_case.execute(request)

        assert exception_info.type is InvalidCategoryData
        
        request.name = "a"*256
        with pytest.raises(InvalidCategoryData, match="name cannot be longer than 255 characters") as exception_info:
            c_id = use_case.execute(request)

        assert exception_info.type is InvalidCategoryData
