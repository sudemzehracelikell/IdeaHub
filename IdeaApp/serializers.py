from rest_framework import serializers
from .models import Category
from .models import Update

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']




class UpdateSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Update
        fields = ['id', 'user', 'update_text', 'created_at']


#Backend’deki veritabanı modellerini (ör. Comment, Idea, Vote) frontend’in anlayacağı JSON formatına çevirir.
#Kullanıcı frontend üzerinden veri gönderdiğinde (POST request gibi), serializer bu JSON veriyi doğrular ve model objesine çevirir.