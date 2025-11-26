from django.urls import path
from .views import UpdateView

urlpatterns = [
    path('ideas/<int:idea_id>/updates/', UpdateView.as_view(), name='idea-updates'),
]
#urls.py, Django’da HTTP isteklerini doğru view’a yönlendiren sistemdir.