from django.views import View
from django.http import JsonResponse
from .services import CategoryService  # Aynı klasör içinden
import json
from .models import Category
from .services import UpdateService
import json
from .models import Update
import json

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

class UpdateView(View):
    service = UpdateService()

    def get(self, request, idea_id):
        idea = Idea.objects.get(id=idea_id)
        updates = self.service.list(idea)
        data = [{"id": u.id, "text": u.update_text, "created_at": u.created_at} for u in updates]
        return JsonResponse(data, safe=False)

    def post(self, request, idea_id):
        body = json.loads(request.body)
        idea = Idea.objects.get(id=idea_id)
        update = self.service.add(request.user, idea, body['text'])
        return JsonResponse({"id": update.id, "text": update.update_text})