from django.contrib import admin
from .models import Article, Comment

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk','title','content','created_at','updated_at',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk','content','created_at','updated_at',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)