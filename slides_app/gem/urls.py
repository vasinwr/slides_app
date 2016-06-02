from django.conf.urls import url

from . import views

app_name = 'gem'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^getjson', views.getjson, name='get json'),
]
 
