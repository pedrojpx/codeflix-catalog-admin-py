from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category import InMemoryCategoryRepository


class TestInMemoryCategory:
    def test_can_save_category(self):
        repo = InMemoryCategoryRepository()
        category = Category(
            name="Filme",
            description="categoria de filmes"
        )
        repo.save(category)

        assert len(repo.categories)
        assert repo.categories[0] == category
