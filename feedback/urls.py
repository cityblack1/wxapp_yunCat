from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from feedback import views

urlpatterns = [
    url(r'^contact/$', views.ContactList.as_view()),
    url(r'^contact/(?P<pk>[0-9]+)/$', views.ContactDetail.as_view()),
    url(r'^feedback/$', views.FeedBackList.as_view()),
    url(r'^contact/(?P<pk>[0-9]+)/$', views.FeedBackDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)