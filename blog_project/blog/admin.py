# admin.py

from django.contrib import admin
from .models import Category, Tag, Post, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
   readonly_fields = ('created', 'updated')  
   list_display = ('name', 'active', 'created') 
   search_fields = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')
    search_fields = ('name',)
    list_filter = ('active',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'excerpt', 'created_at', 'category')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'author', 'category')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at')
    search_fields = ('content',)
    list_filter = ('created_at', 'author')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
