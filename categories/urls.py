from django.urls import path
from .views import CategoryListCreate, CategoryDetail

urlpatterns = [
      path('categories/', CategoryListCreate.as_view(), name='category-list-create'),
      path('categories/<int:pk>', CategoryDetail.as_view(), name='category-detail'),
]