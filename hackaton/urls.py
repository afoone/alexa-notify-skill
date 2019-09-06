from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

# Create your models here.


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('alexa/', include('seguroencasa.urls'))
]
