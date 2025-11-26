from IdeaProject.InteractionApp.CommentApp import models
from IdeaProject.UserApp.models import User



class Update(models.Model):
    class State(models.TextChoices):
        IN_PROGRESS = "IN_PROGRESS", "Devam Ediyor"
        COMPLETED = "COMPLETED", "Tamamlandı"
        WAITING = "WAITING", "Beklemede"
        CANCELLED = "CANCELLED", "İptal Edildi"

    id = models.AutoField(primary_key=True)
    state = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="updates")
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name="updates")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Update for {self.idea.title}"