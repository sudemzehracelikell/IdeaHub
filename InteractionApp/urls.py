from django.urls import path
from .views import CommentView
from .views import VoteView

urlpatterns = [
    path('ideas/<int:idea_id>/comments/', CommentView.as_view(), name='idea-comments'),
]

urlpatterns = [
    path('ideas/<int:idea_id>/vote/', VoteView.as_view(), name='idea-vote'),
]
