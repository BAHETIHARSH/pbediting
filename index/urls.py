from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name='index'),
path('about', views.about, name='about'),
path('blog', views.blog, name='blog'),
path('tutorials', views.tutorials, name='tutorials'),
path('tutorials_cs3', views.tutorials_cs3, name='tutorials'),
path('tutorials_cc', views.tutorials_cc, name='tutorials'),
path('contact', views.contact, name='contact'),
path('search', views.search, name='search'),
]
