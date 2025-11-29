from django.urls import path
from .views import CategoryListView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
]
from django.urls import path
from .views import UpdateView

urlpatterns = [
    path('ideas/<int:idea_id>/updates/', UpdateView.as_view(), name='idea-updates'),
]
