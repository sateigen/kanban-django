from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'board/(?P<board_id>[0-9]+)/$', views.board_detail, name='board_detail'),
    url(r'register/$', views.register, name='register'),
]
