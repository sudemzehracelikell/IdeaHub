from django.urls import path
from .views import CommentView

urlpatterns = [
    path('ideas/<int:idea_id>/comments/', CommentView.as_view(), name='idea-comments'),
]
