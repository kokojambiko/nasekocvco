from django.urls import path
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'base'

urlpatterns = [
    path('', views.Main.as_view(), name='home'),
    path('orders/', orders_list, name='orders'),
    path('orders/<int:pk>/edit/',views.order_edit,name='order_edit'),
    path('orders/new/', views.order_create, name='order_create'),
    path('orders/<int:pk>/delete/',views.order_delete,name='order_delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)