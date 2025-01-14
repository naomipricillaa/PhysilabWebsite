from django.views.generic import TemplateView
from users.views import index_page, landing_page
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  # Include the users app's URLs
    path('', index_page, name='index'),
    path('landing/', landing_page, name='landing')
]