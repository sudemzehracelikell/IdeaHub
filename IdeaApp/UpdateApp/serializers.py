from rest_framework import serializers
from .models import Update

class UpdateSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Update
        fields = ['id', 'user', 'update_text', 'created_at']


#Backend’deki veritabanı modellerini (ör. Comment, Idea, Vote) frontend’in anlayacağı JSON formatına çevirir.
#Kullanıcı frontend üzerinden veri gönderdiğinde (POST request gibi), serializer bu JSON veriyi doğrular ve model objesine çevirir.