

from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from . import views

urlpatterns = [
    path('login/',views.app_login,name='login'),
    path('logout/',views.app_logout,name='logout'),
    path('register/',views.app_register_from,name='register'),
    path('edituser_form/',views.edituser_form,name='edituser_form'),
    path('cpass/',views.app_changepass,name='cpass'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
