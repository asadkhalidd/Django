from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('billing/', views.billing, name='billing'),
    path('notifications/', views.notifications, name='notifications'),
    path('profile/', views.profile, name='profile'),
    path('rtl/', views.rtl, name='rtl'),
    path('sign-in/', views.signin, name='signin'),
    path('sign-up/', views.signup, name='signup'),
    path('virtual-reality/', views.virtualreality, name='virtualreality'),



    path('user_form/', views.user_form, name="user_insert"),
    path('<int:id>/', views.user_form, name="user_update"),
    path('delete/<int:id>/',views.user_delete,name='user_delete'),
    path('user_list/', views.user_list, name='user_list'),
    
    
]