from users_app import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.forms import UserCreationForm


urlpatterns = [
    path('sign', views.sign, name = 'sign'),
    path('login', views.login, name = 'login')
    
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
