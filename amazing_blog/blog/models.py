from django.core.urlresolvers import reverse
from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    intro = models.TextField()
    mas = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post)
    comment = models.TextField()
