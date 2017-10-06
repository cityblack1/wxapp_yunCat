from django.db import models

from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=24, verbose_name='名称')
    describe = models.TextField(verbose_name='描述', blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name


class PublishManager(models.Manager):
    def get_queryset(self):
        return super(PublishManager, self).get_queryset().filter(status='publish')


STAT = (
    ('publish', '发布'),
    ('draft', '草稿')
)


class Articles(models.Model):
    title = models.CharField(max_length=48, verbose_name='标题')
    content = models.TextField(verbose_name='正文')
    cover_img = models.ImageField(null=True, blank=True, verbose_name='封面图')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    updated = models.DateTimeField(auto_now=True, verbose_name='修改日期')
    author = models.CharField(max_length=24, verbose_name='作者', default='Sidhush')
    category = models.ForeignKey(Category, verbose_name='分类', null=True, blank=True)
    tags = TaggableManager()
    published = PublishManager()
    status = models.CharField(choices=STAT, max_length=10, default='draft')

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return self.title


