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
        blg = BlogPost.objects.get(pk=self.pk)
        cmts = blg.comment_set.all()
        len_cmts = len(cmts)*2
        blg.pk = None
        blg.save()
        
        if cmts:
            for cmt in cmts:
                cmt.pk = None
                cmt.blog_post = blg
                cmt.save()

        return blg.id


class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
