from .models import Vote

class VoteService:
    def add(self, user, idea):
        # Kullanıcı aynı fikre ikinci kez oy veremez
        vote, created = Vote.objects.get_or_create(user=user, idea=idea)
        return vote if created else None

    def count(self, idea):
        # Bir fikre ait toplam oy sayısı
        return Vote.objects.filter(idea=idea).count()
