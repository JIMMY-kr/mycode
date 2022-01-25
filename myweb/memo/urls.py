from memo import views
from django.urls import path
#http://localhost/memo
#공통적인 memo페이지의 url
urlpatterns=[
    path('',views.home),
    path('insert_memo', views.insert_memo),
    path('detail', views.detail_memo),
    path('update_memo', views.update_memo),
    path('delete_memo', views.delete_memo),
]