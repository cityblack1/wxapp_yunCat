from django.conf.urls import url, include
# from .views import delete


urlpatterns = [
    url(r'^images/', include('cat_images.urls')),
]