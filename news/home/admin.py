from django.contrib import admin
from .models import News, Category, Tags
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'create_at', 'user', 'view_count', 'category']
    readonly_fields = ['view_count', ]
    prepopulated_fields = {'slug': ('title',), }

admin.site.register(News, NewsAdmin)
admin.site.register(Category)
admin.site.register(Tags)


# Register your models here.