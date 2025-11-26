from django.contrib import admin
from .models import Category

@admin.register(Category) #Admin’e otomatik kayıt işlemini gerçekleştirir.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name","created_at") #Admin panelindeki tablo sütunlarını belirler.
    search_fields = ("name",)  #Hızlı arama çubuğunda aranabilir alanlar.
    ordering = ("id",) #Sağ tarafta filtreleme bölümü oluşturur.
    readonly_fields = ("created_at",) #Tarihlerin kullanıcı tarafında değiştirilememesini sağlar.
