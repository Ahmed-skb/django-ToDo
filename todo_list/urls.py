from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('cross_off/<list_id>', views.cross_off, name='cross_off'),
    path('edit/<list_id>', views.edit, name='edit'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
]
