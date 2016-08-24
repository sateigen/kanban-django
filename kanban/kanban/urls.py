from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from rest_framework import routers
from board import views


router = routers.DefaultRouter()
router.register(r'board', views.BoardViewSet)
router.register(r'ticket', views.TicketViewSet)
router.register(r'task', views.TaskViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^', include('board.urls')),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
]
