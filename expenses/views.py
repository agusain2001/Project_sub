from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Expense
from .serializers import ExpenseSerializer
from utils.permissions import IsOwnerOrReadOnly
from utils.custom_errors import NotFoundError, CustomValidationError
from utils.helpers import paginate_response, CustomPagination


class ExpenseListCreate(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        expenses = Expense.objects.all()
        return paginate_response(expenses, request, ExpenseSerializer)

    def post(self, request):
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        raise CustomValidationError("Validation Error", serializer.errors)

class ExpenseDetail(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            return Expense.objects.get(pk=pk)
        except Expense.DoesNotExist:
            raise NotFoundError("Expense not found")


    def get(self, request, pk):
        expense = self.get_object(pk)
        serializer = ExpenseSerializer(expense)
        return Response(serializer.data)

    def put(self, request, pk):
         expense = self.get_object(pk)
         serializer = ExpenseSerializer(expense, data=request.data)
         if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
         raise CustomValidationError("Validation Error", serializer.errors)


    def delete(self, request, pk):
        expense = self.get_object(pk)
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def MonthlyAnalysis(request):
    month = request.query_params.get('month')
    if not month:
      raise InvalidInputError("Please provide the month")
    try:
       month = int(month)
       if month < 1 or month > 12:
           raise InvalidInputError("Please provide a valid month")
    except:
       raise InvalidInputError("Please provide a valid month")
    expenses = Expense.objects.filter(date__month=month, created_by=request.user)
    expenses_by_category = {}
    for expense in expenses:
         if expense.category.name in expenses_by_category:
            expenses_by_category[expense.category.name] += float(expense.amount)
         else:
             expenses_by_category[expense.category.name] = float(expense.amount)
    return Response({
        "expenses_by_category": expenses_by_category
     }, status=status.HTTP_200_OK)














