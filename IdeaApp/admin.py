from django.contrib import admin
from .models import Category
from .models import Update

@admin.register(Category) #Admin’e otomatik kayıt işlemini gerçekleştirir.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name","created_at") #Admin panelindeki tablo sütunlarını belirler.
    search_fields = ("name",)  #Hızlı arama çubuğunda aranabilir alanlar.
    ordering = ("id",) #Sağ tarafta filtreleme bölümü oluşturur.
    readonly_fields = ("created_at",) #Tarihlerin kullanıcı tarafında değiştirilememesini sağlar.



@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
    list_display = ("id", "idea", "user", "state", "created_at")
    list_filter = ("state", "created_at")
    search_fields = ("idea__title", "user__username", "description")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)
