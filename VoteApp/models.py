from django.db import models
from IdeaProject.CommentApp import models
from IdeaProject.UserApp.models import User


class Vote(models.Model):
    id = models.AutoField(primary_key=True)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name="votes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="votes")
    value = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} voted {self.value} on {self.idea.title}"