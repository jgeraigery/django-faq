# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('status', models.IntegerField(default=1, help_text='Only objects with "published" status will be displayed publicly.', db_index=True, verbose_name='status', choices=[(1, 'drafted'), (2, 'published'), (3, 'removed')])),
                ('question', models.CharField(max_length=255, verbose_name='question')),
                ('slug', models.SlugField(help_text='Used in         the URL for the Question. Must be unique.', unique=True, verbose_name='slug')),
                ('answer', models.TextField(verbose_name='answer')),
                ('ordering', models.PositiveSmallIntegerField(help_text='An integer used to order the question             amongst others related to the same topic. If not given this             question will be last in the list.', db_index=True, verbose_name='ordering', blank=True)),
            ],
            options={
                'ordering': ('ordering', 'question', 'slug'),
                'abstract': False,
                'get_latest_by': 'modified',
                'verbose_name': 'question',
                'verbose_name_plural': 'questions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('status', models.IntegerField(default=1, help_text='Only objects with "published" status will be displayed publicly.', db_index=True, verbose_name='status', choices=[(1, 'drafted'), (2, 'published'), (3, 'removed')])),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', models.SlugField(help_text='Used in         the URL for the topic. Must be unique.', unique=True, verbose_name='slug')),
                ('description', models.TextField(help_text='A short description of this topic.', verbose_name='description', blank=True)),
                ('sites', models.ManyToManyField(related_name='faq_topics', verbose_name='sites', to='sites.Site')),
            ],
            options={
                'ordering': ('title', 'slug'),
                'abstract': False,
                'get_latest_by': 'modified',
                'verbose_name': 'topic',
                'verbose_name_plural': 'topics',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='question',
            name='topic',
            field=models.ForeignKey(related_name='questions', verbose_name='topic', to='faq.Topic'),
            preserve_default=True,
        ),
    ]
