from uuid import UUID

import pytest
from src.core.category.application.create_category import CreateCategoryRequest, CreateCategoryUseCase
from src.core.category.application.exceptions import InvalidCategoryData
from src.core.category.infra.in_memory_category import InMemoryCategoryRepository


class TestCreateCategory:
    def test_create_w_valid_data(self):
        repo = InMemoryCategoryRepository()
        use_case = CreateCategoryUseCase(repo)
        request = CreateCategoryRequest(
            name="Filme", 
            description="Categoria para filmes", 
            is_active=True
        )

        response = use_case.execute(request)

        assert response is not None
        assert isinstance(response.id, UUID)
        assert len(repo.categories) == 1
        assert repo.categories[0].id == response.id
        assert repo.categories[0].description == "Categoria para filmes"
        assert repo.categories[0].is_active == True
    
    def test_create_w_invalid_data(self):
        repo = InMemoryCategoryRepository()
        use_case = CreateCategoryUseCase(repo)
        request = CreateCategoryRequest(
            name="", 
            description="Categoria para filmes", 
            is_active=True
        )

        with pytest.raises(InvalidCategoryData, match="name cannot be empty"):
            response = use_case.execute(request)
            assert response is None

        assert len(repo.categories) == 0