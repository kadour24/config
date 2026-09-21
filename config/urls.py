"""
https://www.facebook.com/profile/

http://localhost:8000/core/

http://localhost:8000/core/settings/

"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),

]
