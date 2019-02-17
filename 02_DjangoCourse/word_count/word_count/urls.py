from django.contrib import admin
from django.urls import path
from word_count import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home_page'),
    path('count_result/', views.count_page, name='count_result'),
    path('first/', views.first_page),
    path('second/', views.second_page),
]
