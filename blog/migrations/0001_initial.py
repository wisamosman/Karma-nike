# Generated by Django 4.2.7 on 2023-11-07 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('subtitle', models.TextField(max_length=30)),
                ('description', models.TextField(max_length=300)),
                ('image', models.ImageField(upload_to='blog')),
                ('create_data', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment', models.TextField(max_length=50)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_blog', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]