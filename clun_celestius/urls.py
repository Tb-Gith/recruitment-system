from django.contrib import admin
from django.urls import path, include   # <-- include must be imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applications.urls')),  # mount your app's urls at the project root
]
