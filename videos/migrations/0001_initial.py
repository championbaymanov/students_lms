# Generated by Django 4.0.4 on 2022-05-30 14:06

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='VideoContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
                ('vidoe_url', models.URLField()),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('published', models.BooleanField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.authorvideo')),
                ('categories', models.ManyToManyField(to='videos.category')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('content', models.TextField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.videocontent')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
