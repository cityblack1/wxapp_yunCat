import os
from PIL import Image

from django.db import models
from django.contrib.auth.models import User
from django.core.files.base import ContentFile


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='publish')

STATUS = (('draft', '草稿'), ('publish', '出版'))


class CatImage(models.Model):
    title = models.CharField(max_length=48, verbose_name='标题', blank=True)
    image_url = models.CharField(max_length=256, verbose_name='链接地址')
    image = models.ImageField(upload_to='cat', verbose_name='图片', null=True, blank=True)
    like_nums = models.IntegerField(verbose_name='点赞数', default=0)
    created = models.DateTimeField(auto_now_add=True)
    width = models.IntegerField(default=0, verbose_name='图片宽度')
    height = models.IntegerField(default=0, verbose_name='图片高度')
    status = models.CharField(choices=STATUS, verbose_name='状态', max_length=8, default='draft')
    uploader = models.ForeignKey(User, default=1, related_name='uploader')
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ('created', )

    def __str__(self):
        return self.image_url

    def save_image(self, image_name='', response='', *args, **kwargs):
        try:
            content = ContentFile(response)
            self.image.save(image_name, content, save=False)
        except:
            return None
        # self.image.save('cat.jpg', ContentFile(response.content), save=False)
        self.save()

    def zip_images(self):
        image = Image.open(self.image)  # 通过cp.picture 获得图像
        width = image.width
        height = image.height
        rate = 1.0  # 压缩率

        # 根据图像大小设置压缩率
        if width >= 2000 or height >= 2000:
            rate = 0.3
        elif width >= 1000 or height >= 1000:
            rate = 0.5
        elif width >= 500 or height >= 500:
            rate = 0.9

        width = int(width * rate)  # 新的宽
        height = int(height * rate)  # 新的高
        self.width = width
        self.height = height

        image.thumbnail((width, height), Image.ANTIALIAS)  # 生成缩略图
        image.save(os.path.join(DIR, 'new') + str(self.image))  # 保存到原路径
        self.save()

    def save_zip(self, *args, **kwargs):
        try:
            image = self.image.file.name
        except:
            image = None
        try:
            if image:
                name = self.image.file.name
                with Image.open(self.image) as image: # 通过cp.picture 获得图像
                    width = image.width
                    height = image.height
                    rate = 1.0  # 压缩率

                    # 根据图像大小设置压缩率
                    if width >= 2000 or height >= 2000:
                        rate = 0.3
                    elif width >= 1000 or height >= 1000:
                        rate = 0.5
                    elif width >= 500 or height >= 500:
                        rate = 0.9

                    width = int(width * rate)  # 新的宽
                    height = int(height * rate)  # 新的高
                    self.width = width
                    self.height = height

                    image.thumbnail((width, height), Image.ANTIALIAS)
                    image.save(name)
                    self.save()
        except Exception as e:
            print(e)


class UserImage(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, verbose_name='上传用户')
    location = models.CharField(max_length=128, blank=True, verbose_name='发现地点')
    created = models.DateField(auto_now_add=True, verbose_name='创建时间')
    describe = models.CharField(max_length=256, blank=True, verbose_name='描述')
    image = models.ImageField(upload_to='user_update/%Y/%m', null=True, blank=True, verbose_name='图片')



