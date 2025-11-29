from django.db import models

from UserApp import models
from UserApp.models import User
from InteractionApp import models

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    idea = models.ForeignKey('ideas.Idea', on_delete=models.CASCADE,related_name='comments') # Hangi fikir için yorum yapıldığı
    user = models.ForeignKey(User, on_delete=models.CASCADE)      # Yorumu yapan kullanıcı


    def __str__(self):
        return f"{self.user.username} - {self.text[:20]}"



class Vote(models.Model):
    id = models.AutoField(primary_key=True)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name="votes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="votes")
    value = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} voted {self.value} on {self.idea.title}"

