from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCount
from taggit.managers import TaggableManager

# Create your models here.

User = get_user_model()

class Author_Register(models.Model):
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

class Register(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    post = models.ForeignKey('Open_lessons', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.full_name


class Open_lessons(models.Model):
    title = models.CharField(max_length=100)
    additional = models.TextField()
    slug = AutoSlugField(populate_from='title')
    slug_register = AutoSlugField(populate_from='title')
    phota = models.ImageField(upload_to="", null=True, blank=True)
    date_of_the_event = models.DateTimeField()
    spiker = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    description = models.TextField()
    for_information = models.CharField(max_length=30)
    author = models.ForeignKey(Author_Register, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    published = models.BooleanField()
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    tags = TaggableManager()
    @property
    def open_lesson_link(self):
        return reverse("open_lesson", kwargs={
            'slug': self.slug
        })

    def __str__(self):
        return self.title

    @property
    def open_lesson_link_register(self):
        return reverse("open_lesson_register", kwargs={
            'slug': self.slug
        })

    def __str__(self):
        return self.title