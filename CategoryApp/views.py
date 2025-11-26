from django.views import View
from django.http import JsonResponse
from .services import CategoryService  # Aynı klasör içinden
import json
from .models import Category

class CategoryListView(View):
    service = CategoryService()

    def get(self, request):
        categories = self.service.list()
        data = [{"id": c.id, "name": c.name, "description": c.description} for c in categories]
        return JsonResponse(data, safe=False)

    def post(self, request):
        body = json.loads(request.body)
        category = self.service.create(body['name'], body.get('description'))
        return JsonResponse({"id": category.id, "name": category.name})


""" GET: Kategori listesini döner.
    POST: Yeni kategori ekler.
"""