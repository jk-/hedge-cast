from app.models.category import Category
from app.database import Repository


class CategoryRepository(Repository):
    __model__ = Category
