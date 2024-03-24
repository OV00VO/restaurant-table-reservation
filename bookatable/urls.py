from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('about/', views.about, name='about'),
    
    path('reservation/', views.create_reservation, name='create_reservation'),
    path('read_reservation/<int:reservation_id>/', views.read_reservation, name='read_reservation'),
    path('update_reservation/<int:reservation_id>/', views.update_reservation, name='update_reservation'),
    path('delete_reservation/<int:reservation_id>/', views.delete_reservation, name='delete_reservation'),
    path('reservation/success/', views.reservation_success, name='reservation_success'),
    path('reservations/', views.list_reservation, name='reservation_list'),
    
    path('contact/', views.contact, name='contact'),
   
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('record/', views.record, name='record'),
    
    path('create_reservation/', views.record, name='create'),
    path('read_reservation/', views.record, name='read'),
    path('update_reservation', views.record, name='update'),
    path('delete_reservation/', views.record, name='delete'),
    
    path('my_reservations/', views.my_reservations, name='my_reservations'),
    path('update_user_info', views.record, name='update'),
    
    path('test_crud/', views.test_crud, name='test_crud'),
]