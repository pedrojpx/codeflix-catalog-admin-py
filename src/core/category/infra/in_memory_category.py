from uuid import UUID
from src.core.category.application.category_repository import CategoryRepository
from src.core.category.domain.category import Category
from src.core.category.application.use_cases.exceptions import CategoryNotFound


class InMemoryCategoryRepository(CategoryRepository):
    def __init__(self, categories=None):
        self.categories = categories or []

    def save(self, category):
        self.categories.append(category)

    def get_by_id(self, id: UUID) -> Category:
        for c in self.categories:
            if c.id == id:
                return c

        return None