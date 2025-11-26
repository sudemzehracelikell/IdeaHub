from rest_framework import serializers
from .models import Vote

class VoteSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Vote
        fields = ['id', 'user', 'created_at']
