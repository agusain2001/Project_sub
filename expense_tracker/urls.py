from django.contrib import admin
from django.urls import path, include

urlpatterns = [
      path('admin/', admin.site.urls),
      path('api/', include('users.urls')),
      path('api/', include('expenses.urls')),
      path('api/', include('groups.urls')),
      path('api/', include('settlements.urls')),
      path('api/', include('categories.urls')),
  ]