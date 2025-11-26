from IdeaProject.UserApp import models
from IdeaProject.UserApp.models import User


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    idea = models.ForeignKey('ideas.Idea', on_delete=models.CASCADE,related_name='comments') # Hangi fikir için yorum yapıldığı
    user = models.ForeignKey(User, on_delete=models.CASCADE)      # Yorumu yapan kullanıcı


    def __str__(self):
        return f"{self.user.username} - {self.text[:20]}"
