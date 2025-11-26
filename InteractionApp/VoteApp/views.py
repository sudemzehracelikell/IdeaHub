from django.views import View
from django.http import JsonResponse
from .services import VoteService
from IdeaApp.models import Idea

class VoteView(View):

    service = VoteService()

    def post(self, request, idea_id):
        # Idea nesnesini al
        idea = Idea.objects.get(id=idea_id)
        vote = self.service.add(request.user, idea)
        if vote:
            total_votes = self.service.count(idea)
            return JsonResponse({"status": "success", "total_votes": total_votes})
        return JsonResponse({"status": "failed", "message": "Already voted"})