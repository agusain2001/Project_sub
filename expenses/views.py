from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Expense
from .serializers import ExpenseSerializer
from utils.permissions import IsOwnerOrReadOnly


class ExpenseListCreate(APIView):
     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
     def get(self, request):
         expenses = Expense.objects.all()
         serializer = ExpenseSerializer(expenses, many=True)
         return Response(serializer.data)

     def post(self, request):
         serializer = ExpenseSerializer(data=request.data)
         if serializer.is_valid():
             serializer.save(created_by = request.user)
             return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExpenseDetail(APIView):
     permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

     def get_object(self, pk):
         try:
             return Expense.objects.get(pk=pk)
         except Expense.DoesNotExist:
             return None

     def get(self, request, pk):
         expense = self.get_object(pk)
         if expense is None:
           return Response({"error": "Not Found"},status=status.HTTP_404_NOT_FOUND)
         serializer = ExpenseSerializer(expense)
         return Response(serializer.data)
     def put(self, request, pk):
         expense = self.get_object(pk)
         if expense is None:
           return Response({"error": "Not Found"},status=status.HTTP_404_NOT_FOUND)
         serializer = ExpenseSerializer(expense, data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     def delete(self, request, pk):
        expense = self.get_object(pk)
        if expense is None:
           return Response({"error": "Not Found"},status=status.HTTP_404_NOT_FOUND)
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)