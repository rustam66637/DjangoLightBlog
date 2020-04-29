from time import time

from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse

from django.utils.text import slugify

def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return  new_slug + '-' + str(int(time()))

class Post(models.Model):
    '''Posts'''
    # author = models.ForeignKey(
    #     User,
    #     verbose_name='Автор',
    #     on_delete=models.CASCADE,
    #     related_name='posts',
    # )
    title = models.CharField('Заголовок', max_length=150, db_index=True)
    slug = models.SlugField('URL', max_length=100, unique=True, blank=True)
    text = models.TextField('Описание', max_length=5000, db_index=True)
    publish_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    tags = models.ManyToManyField(
        'Tag',
        blank=True,
        related_name='posts',
    )

    def get_absolute_url(self):
        '''ссылка на конкретный объект типа post'''
        # регенерация ссылки на объект
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        '''если слаг не прописан - генерировать слаг'''
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('-publish_date',)
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    slug = models.SlugField('URL', max_length=50, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})


    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
