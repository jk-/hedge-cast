from app.models.category import Category
from app.database import Repository


class CategoryRepository(Category, Repository):
    @staticmethod
    def get_by_name(name):
        if isinstance(name, str):
            return Category.query.filter_by(name=name).first()
        return None
