from django.contrib import admin
from django.urls import path
from newsapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('fetch/', views.fetch_news_view, name='fetch_news'),
]