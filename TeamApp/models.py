from django.db import models

from UserApp.models import User

class TeamMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.userName

class Team(models.Model):
    teamName = models.CharField(max_length=100)
    teamMember = models.ManyToManyField(TeamMember)
    #idea = models.ManyToManyField(Idea)

    def __str__(self):
        return self.teamName