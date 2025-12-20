from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json

from IdeaApp.services import CategoryService, UpdateService

from .models import Idea, Status, Tag, Media, Category, Team

@method_decorator(csrf_exempt, name='dispatch')
class IdeaView(View):
    def get(self, request):
        ideas = Idea.objects.all()
        data = []
        for idea in ideas:
            data.append({
                "id": idea.IdeaID,
                "title": idea.Title,
                "description": idea.Description,
                "short_description": idea.ShortDescription,
                "votes": idea.VotesCount,
                "created_at": idea.CreateDate,
                "creator": idea.CreaterID.username if idea.CreaterID else "Unknown",
                "status": idea.StatusID.name if idea.StatusID else "None",
                "category": idea.CategoryID.name if idea.CategoryID else "None",
                "team": idea.TeamID.name if idea.TeamID else "None", 
                "tags": [tag.TagName for tag in idea.Tags.all()]
            })
        return JsonResponse(data, safe=False)

    def post(self, request):
        try:
            body = json.loads(request.body)
            user = User.objects.get(id=body['user_id'])
            category = Category.objects.get(id=body['category_id'])
            team = Team.objects.get(id=body['team_id'])
            status = None
            if 'status_id' in body:
                status = Status.objects.get(id=body['status_id'])

            new_idea = Idea.objects.create(
                Title=body['title'],
                Description=body['description'],
                ShortDescription=body.get('short_description', ''),
                CreaterID=user,      
                CategoryID=category, 
                TeamID=team,       
                StatusID=status     
            )

            if 'tag_ids' in body:
                tags = Tag.objects.filter(TagID__in=body['tag_ids'])
                new_idea.Tags.set(tags)

            return JsonResponse({"message": "Idea added.", "id": new_idea.IdeaID}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class StatusView(View):
    def get(self, request):
        statuses = Status.objects.all()
        data = [{"id": s.id, "name": s.name} for s in statuses]
        return JsonResponse(data, safe=False)

    def post(self, request):
        try:
            body = json.loads(request.body)
            new_status = Status.objects.create(name=body['name'])
            return JsonResponse({"message": "Status added.", "id": new_status.id}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
        
@method_decorator(csrf_exempt, name='dispatch')
class TagView(View):
    def get(self, request):
        tags = Tag.objects.all()
        data = [{"id": t.TagID, "name": t.TagName} for t in tags]
        return JsonResponse(data, safe=False)

    def post(self, request):
        try:
            body = json.loads(request.body)
            new_tag = Tag.objects.create(TagName=body['name'])
            return JsonResponse({"message": "Tag added.", "id": new_tag.TagID}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class MediaView(View):
    def get(self, request):
        medias = Media.objects.all()
        data = []
        for m in medias:
            data.append({
                "id": m.MediaID,
                "type": m.MediaType,
                "path": str(m.MediaPath),
                "idea": m.IdeaID.Title if m.IdeaID else "None"
            })
        return JsonResponse(data, safe=False)

    def post(self, request):
        try:
            body = json.loads(request.body)
            idea = Idea.objects.get(IdeaID=body['idea_id'])
            
            new_media = Media.objects.create(
                MediaType=body['type'],
                IdeaID=idea,
                MediaPath=body.get('path', 'default.jpg')
            )
            return JsonResponse({"message": "Media added.", "id": new_media.MediaID}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

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
