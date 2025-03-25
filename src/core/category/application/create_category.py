from uuid import UUID

from core.category.infra.in_memory_category import InMemoryCategoryRepository
from src.core.category.domain.category import Category

def create_category(
        repository: InMemoryCategoryRepository,
        name: str, 
        description: str = "", 
        is_active: bool = True) -> UUID:
    try:
        c = Category(name=name, description=description, is_active=is_active)
    except ValueError as err:
        raise InvalidCategoryData(err)
    
    repository.save(c)
    return c.id

class InvalidCategoryData(Exception):
    pass