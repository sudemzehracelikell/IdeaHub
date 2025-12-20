from django.urls import path
from .views import CategoryListView, UpdateView, IdeaView, StatusView, TagView, MediaView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('ideas/<int:idea_id>/updates/', UpdateView.as_view(), name='idea-updates'),
    path('ideas/', IdeaView.as_view(), name='idea-list'),
    path('status/', StatusView.as_view(), name='status-list'),
    path('tags/', TagView.as_view(), name='tag-list'),
    path('media/', MediaView.as_view(), name='media-list'),
]
