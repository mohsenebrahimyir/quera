#!/usr/bin/python3
# Github: https://github.com/mohsenebrahimyir/quera

### https://quera.ir/problemset/14742/ ###

from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.date_created}"

    def copy(self):
        post = BlogPost.objects.get(pk=self.pk)
        comments = post.comment_set.all()

        post.pk = None
        post.save()

        for comment in comments:
            comment.pk = None
            comment.blog_post = post
            comment.save()

        return post.id


class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.text} - {self.blog_post}"
