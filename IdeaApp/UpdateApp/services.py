from .models import Update

class UpdateService:
    def add(self, user, idea, text):
        # Yeni güncelleme ekler
        return Update.objects.create(user=user, idea=idea, update_text=text)

    def list(self, idea):
        # Belirli bir fikre ait tüm güncellemeleri listeler
        return Update.objects.filter(idea=idea).order_by('-created_at')