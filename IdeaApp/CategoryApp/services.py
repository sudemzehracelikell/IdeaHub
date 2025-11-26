from .models import Category

class CategoryService:

    def create(self, name, description=None):
        return Category.objects.create(name=name, description=description)

    def list(self):
        return Category.objects.all()

    def get(self, category_id):
        return Category.objects.get(id=category_id)

    def update(self, category_id, **kwargs):
        category = Category.objects.get(id=category_id)
        for key, value in kwargs.items():
            setattr(category, key, value)
        category.save()
        return category

    def delete(self, category_id):
        category = Category.objects.get(id=category_id)
        category.delete()
        return True
