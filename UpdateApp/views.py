from django.views import View
from django.http import JsonResponse
from .services import UpdateService
from IdeaApp.models import Idea
import json
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