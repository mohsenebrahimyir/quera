import imp
from django.contrib import admin
from .models import Author, BlogPost, Comment 


admin.site.register(Author)
admin.site.register(BlogPost)
admin.site.register(Comment)