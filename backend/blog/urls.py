from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    # re_path(r'^articles/$', views.article_list),
    # re_path(r'^articles/(?P<pk>[0-9]+)$', views.article_detail),
    re_path(r'^articles/$', views.ArticleList.as_view(), name='article-list'),
    re_path(r'^articles/(?P<pk>\d+)$', views.ArticleDetail.as_view(), name='article-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
