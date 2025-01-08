from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .models import Category
from .serializers import CategorySerializer
from utils.custom_errors import NotFoundError, CustomValidationError
from utils.helpers import paginate_response
from utils.permissions import IsAdminOrReadOnly

class CategoryListCreate(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        categories = Category.objects.all()
        return paginate_response(categories, request, CategorySerializer)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        raise CustomValidationError("Validation Error", serializer.errors)


class CategoryDetail(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get_object(self, pk):
        try:
             return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
             raise NotFoundError("Category not found")


    def get(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
         category = self.get_object(pk)
         serializer = CategorySerializer(category, data=request.data)
         if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
         raise CustomValidationError("Validation Error", serializer.errors)

    def delete(self, request, pk):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)