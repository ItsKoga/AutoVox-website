from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('invite', views.invite, name='invite'),
    path('docs', views.soon, name='docs'),
    path('status', views.soon, name='status'),
    path('dashboard', views.soon, name='dashboard'),
    path('support', views.support, name='support'),
    path('terms', views.terms, name='terms'),
    path('privacy', views.privacy, name='privacy'),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]