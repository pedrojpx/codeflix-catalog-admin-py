from unittest.mock import MagicMock, create_autospec
from uuid import UUID
import uuid

import pytest

from src.core.category.application.category_repository import CategoryRepository
from src.core.category.application.use_cases.get_category import GetCategoryRequest, GetCategoryUseCase, GetCategoryResponse
from src.core.category.application.use_cases.exceptions import InvalidCategoryData
from src.core.category.domain.category import Category

class TestGetCategory:
    def test_return_found_category(self):
        saved_category = Category(
            name="Filme",
            description="Categoria para filmes",
            is_active=True
        )
        mock_repo = create_autospec(CategoryRepository)
        mock_repo.get_by_id.return_value = saved_category

        use_case = GetCategoryUseCase(mock_repo)
        request = GetCategoryRequest(
            id = uuid.uuid4()
        )

        response = use_case.execute(request)

        assert response is not None
        assert mock_repo.get_by_id.called
        assert response == GetCategoryResponse(
            id=saved_category.id,
            description=saved_category.description,
            is_active=saved_category.is_active,
            name=saved_category.name
        )