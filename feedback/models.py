from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User


HAS_PROCESSED = (('yes', '已处理'), ('no', '未处理'))


class FeedBack(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=48, verbose_name='标题')

    # 一个记录可能对应着任何一个Page模型, 也可能什么都不对应
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(ct_field='content_type', fk_field='object_id')

    content = models.TextField(verbose_name='内容')

    uploader = models.ForeignKey(User, default=1)

    has_processed = models.CharField(choices=HAS_PROCESSED, default='no', max_length=4)


class Contact(models.Model):
    title = models.CharField(max_length=48, verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    created = models.DateTimeField(auto_now_add=True)

    has_processed = models.CharField(choices=HAS_PROCESSED, default='no', max_length=4)

    uploader = models.ForeignKey(User, default=1)
