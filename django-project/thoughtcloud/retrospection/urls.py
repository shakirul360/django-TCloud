from retrospection import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.retro, name = 'retrospection'),
    path('look', views.look, name = 'look'),
    path('submit', views.submit, name = 'submit'),
    path('tcloud', views.tcloud, name = 'tcloud'),
    path('test', views.test, name = 'test'),
    path('login', views.login, name = 'login'),
    path('sign', views.sign, name = 'sign')
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
