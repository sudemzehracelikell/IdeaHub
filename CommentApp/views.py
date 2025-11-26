from django.views import View
from django.http import JsonResponse
from .services import CommentService
from IdeaApp.models import Idea
import json

class CommentView(View):
    service = CommentService()

    def get(self, request, idea_id):
        # Idea nesnesini al
        idea = Idea.objects.get(id=idea_id)
        comments = self.service.list(idea)
        # JSON formatına dönüştür
        data = [{"id": c.id, "user": c.user.username, "text": c.text, "created_at": c.created_at} for c in comments]
        return JsonResponse(data, safe=False)

    def post(self, request, idea_id):
        # JSON verisini al
        body = json.loads(request.body)
        idea = Idea.objects.get(id=idea_id)
        comment = self.service.add(request.user, idea, body['text'])
        return JsonResponse({"id": comment.id, "text": comment.text})