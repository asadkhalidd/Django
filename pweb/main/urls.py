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
    path('tables/', views.tables, name='tables'),
    path('virtual-reality/', views.virtualreality, name='virtualreality'),

]