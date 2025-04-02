import uuid

import pytest
from src.core.category.application.use_cases.get_category import GetCategoryRequest, GetCategoryUseCase, GetCategoryResponse
from src.core.category.application.use_cases.exceptions import CategoryNotFound
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category import InMemoryCategoryRepository


class TestGetCategory:
    def test_get_category_by_id(self):
        saved_category = Category(
            name="Filme",
            description="Categoria para filmes",
            is_active=True
        )
        repo = InMemoryCategoryRepository([saved_category])
        use_case = GetCategoryUseCase(repo)
        request = GetCategoryRequest(
            id = saved_category.id
        )

        response = use_case.execute(request)

        assert response is not None
        assert response == GetCategoryResponse(
            id=saved_category.id,
            name=saved_category.name,
            description=saved_category.description,
            is_active=saved_category.is_active
        )    

    def test_raise_exception_when_category_doesnt_exist(self):
        saved_category = Category(
            name="Filme",
            description="Categoria para filmes",
            is_active=True
        )
        repo = InMemoryCategoryRepository([saved_category])
        use_case = GetCategoryUseCase(repo)
        request = GetCategoryRequest(
            id = uuid.uuid4()
        )

        with pytest.raises(CategoryNotFound) as exc:
            use_case.execute(request)