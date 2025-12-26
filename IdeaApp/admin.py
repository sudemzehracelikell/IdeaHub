from django.contrib import admin
from .models import Category, Status, Media, Tag, Idea, Update

admin.site.register(Idea)
admin.site.register(Category)
admin.site.register(Status)
admin.site.register(Tag)
admin.site.register(Update)
admin.site.register(Media)