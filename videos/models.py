from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from hitcount.models import HitCount
from taggit.managers import TaggableManager
from django.contrib.contenttypes.fields import GenericRelation
from django.urls import reverse



# Create your models here.

User = get_user_model()

class AuthorVideo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to="")

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    post = models.ForeignKey('VideoContent', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.user.username
        
class VideoContent(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    vidoe_url = models.URLField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(AuthorVideo, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    published = models.BooleanField()
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    tags = TaggableManager()

    @property
    def video_link(self):
        return reverse("video", kwargs={
            'slug': self.slug
        })

    def __str__(self):
        return self.title


