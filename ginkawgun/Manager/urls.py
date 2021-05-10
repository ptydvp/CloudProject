from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('addfood/',views.app_add_food, name='add_food'),
    path('menu/<int:res_id>/', views.menu_list, name='menu'),
    path('addfood/',views.app_add_food, name='add_food'),
    path('foodupdate/',views.app_update_food, name='update_food'),
    path('menuupdate/<int:menu_id>/',views.menu_update, name='menu_update'),
    path('menudelete/<int:menu_id>/',views.menu_delete, name='menu_delete'),
    path('add_to_cart/<int:menu_id>/',views.add_cart, name='addtocart'),
    path('delete_order/<int:order_id>/', views.delete_order, name='delete_order'),
    path('success_order/<int:order_id>/', views.success_order, name='success_order'),
    path('plus_order/<int:order_id>/', views.plus_order, name='plus_order'),
    path('minus_order/<int:order_id>/', views.minus_order, name='minus_order'),
    path('feedback/<int:ven_id>/', views.Feedback, name='feedback'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
