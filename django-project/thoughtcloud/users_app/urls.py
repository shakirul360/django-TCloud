from users_app import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('sign', views.sign, name = 'sign'),
    path('login', auth_views.LoginView.as_view(template_name = 'log.html'), name = 'login'),
    path('logout', auth_views.LogoutView.as_view(template_name = 'logout.html'), name = 'logout'),

    
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
