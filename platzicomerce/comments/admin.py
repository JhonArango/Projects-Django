from django.contrib import admin
from comments.models import Comment

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Comment, CommentAdmin)