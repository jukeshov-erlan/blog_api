from django.contrib import admin
from .models import *
from review.models import Comment

# Register your models here.
# admin.site.register(Post)

# class PostAdmin(admin.ModelAdmin):
#     list_display = ['title', 'category']
#     list_filter = ['title', 'created_at']
#     search_fields = ['body', 'title']

# admin.site.register(Post, PostAdmin)

class CommentInLine(admin.TabularInline):
    model = Comment

class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInLine]

admin.site.register(Post, PostAdmin)

admin.site.register(Category)
admin.site.register(Tag)