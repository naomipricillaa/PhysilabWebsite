
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile_view'),
    path('profile/edit/', profile_edit, name='profile_edit'),
    path('index/', index_page, name='index'),
    path('', index_page, name='home'),  # Handle root URL
    path('landing/', landing_page, name='landing_page'),
    path('calc/', calculate_pressure, name='calc'),
    path('clear_history/', clear_history, name='clear_history'),
    path('material/', material_page, name='material'),
]
