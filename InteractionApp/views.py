from django.views import View
from django.http import JsonResponse
from .services import CommentService
from .services import VoteService
from .models import Idea
import json

class CommentView(View):
    service = CommentService()

    def get(self, request, idea_id):
        idea = Idea.objects.get(id=idea_id)
        comments = self.service.list(idea)
        data = [{"id": c.id, "user": c.user.username, "text": c.text, "created_at": c.created_at} for c in comments]
        return JsonResponse(data, safe=False)

    def post(self, request, idea_id):
        body = json.loads(request.body)
        idea = Idea.objects.get(id=idea_id)
        comment = self.service.add(request.user, idea, body['text'])
        return JsonResponse({"id": comment.id, "text": comment.text})


    class VoteView(View):
        service = VoteService()

        def post(self, request, idea_id):
            idea = Idea.objects.get(id=idea_id)
            vote = self.service.add(request.user, idea)
            if vote:
                total_votes = self.service.count(idea)
                return JsonResponse({"status": "success", "total_votes": total_votes})
            return JsonResponse({"status": "failed", "message": "Already voted"})