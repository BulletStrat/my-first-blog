from django.conf.urls import url
from django.contrib import admin

from .views import (
      PostListAPIView,
      PostDetailAPIView,
      PostDeleteAPIView,
      PostUpdateAPIView,
      PostCreateAPIView
)



urlpatterns = [
    url(r'^$', PostListAPIView.as_view(), name='list'),
    url(r'^api/posts/create/$', PostCreateAPIView.as_view(), name='create'),
    url(r'^api/posts/(?P<pk>\d+)/$', PostDetailAPIView.as_view(), name='detail'),
    url(r'^api/posts/(?P<pk>\d+)/edit/$', PostUpdateAPIView.as_view(), name='update'),
    url(r'^api/posts/(?P<pk>\d+)/delete/$', PostDeleteAPIView.as_view(), name='delete'),

]