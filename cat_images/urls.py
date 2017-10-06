from django.conf.urls import url
from .views import cat_image_detail, cat_images_list, upload_images
# from .views import delete


urlpatterns = [
    url(r'^cat-images/$', cat_images_list),
    url(r'cat-images/(?P<pk>\d+)/$', cat_image_detail),
    url(r'upload-images/$', upload_images),
    # url(r'^delete-images/$', delete),
]