from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    ## Autentication ##
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    ## API ##
    path('api/', include('api.urls')),
]