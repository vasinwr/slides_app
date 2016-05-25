from django.conf.urls import url

from . import views 

app_name = 'slides'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index_lecturer/', views.lecturer, name='index lecturer'),
    url(r'^index_student/', views.student, name='index student'),
    url(r'^lecture/next_page/', views.next_page, name='next page'),
    url(r'^lecture/prev_page/', views.prev_page, name='previous page'),
    #lecture/ must be at the bottom otherwise it will always be matched first
    url(r'^lecture/', views.lecture, name='lecture'),
]
