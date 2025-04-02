from unittest.mock import MagicMock
from uuid import UUID

import pytest

from src.core.category.application.category_repository import CategoryRepository
from src.core.category.application.use_cases.create_category import CreateCategoryRequest, CreateCategoryUseCase, InvalidCategoryData
from src.core.category.application.use_cases.exceptions import InvalidCategoryData

class TestCreateCategory:
    def test_create_w_valid_data(self):
        mock_repo = MagicMock(CategoryRepository)
        use_case = CreateCategoryUseCase(mock_repo)
        request = CreateCategoryRequest(
            name="Filme", 
            description="Categoria para filmes", 
            is_active=True
        )

        response = use_case.execute(request)

        assert response is not None
        assert isinstance(response.id, UUID)
        assert mock_repo.save.called
    
    def test_create_w_invalid_data(self):
        mock_repo = MagicMock(CategoryRepository)
        use_case = CreateCategoryUseCase(mock_repo)
        request = CreateCategoryRequest(
            name="", 
            description="Categoria para filmes", 
            is_active=True
        )

        with pytest.raises(InvalidCategoryData, match="name cannot be empty") as exception_info:
            response = use_case.execute(request)

        assert exception_info.type is InvalidCategoryData
        
        request.name = "a"*256
        with pytest.raises(InvalidCategoryData, match="name cannot be longer than 255 characters") as exception_info:
            response = use_case.execute(request)

        assert exception_info.type is InvalidCategoryData
