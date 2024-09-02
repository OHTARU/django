from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('update/', update_profile, name='update_profile'),
    path('delete/', delete_account, name='delete_account'),
    path('', home, name='home'),
]