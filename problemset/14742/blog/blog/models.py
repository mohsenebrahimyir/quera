# Github: https://github.com/mohsenebrahimyir/quera
### https://quera.ir/problemset/14742/ ###

from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)


class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def copy(self):
        blog_post = BlogPost.objects.get(pk=self.id)
        comments = blog_post.comment_set.all()
        len_comment = len(comments)
        blog_post.pk = None
        blog_post.save()

        for comment in comments:
            comment.pk = None
            comment.blog_post = blog_post
            comment.save()

        return blog_post.id


class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
