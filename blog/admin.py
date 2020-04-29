from django.contrib import admin
from .models import Post, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'text', 'publish_date',)
    list_filter = ('title', 'publish_date',)
    search_fields = ('title', 'text',)
    prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('author',)
    date_hierarchy = 'publish_date'

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    list_filter = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}

