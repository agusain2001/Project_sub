from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Settlement
from .serializers import SettlementSerializer
from groups.models import Group
from utils.permissions import IsOwnerOrAdminOrReadOnly
from utils.custom_errors import NotFoundError, CustomValidationError, InvalidInputError
from utils.helpers import paginate_response, calculate_settlement_suggestions
from rest_framework.decorators import api_view

class SettlementListCreate(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        settlements = Settlement.objects.all()
        return paginate_response(settlements, request, SettlementSerializer)

    def post(self, request):
        serializer = SettlementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        raise CustomValidationError("Validation Error", serializer.errors)

class SettlementDetail(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdminOrReadOnly]

    def get_object(self, pk):
        try:
            return Settlement.objects.get(pk=pk)
        except Settlement.DoesNotExist:
            raise NotFoundError("Settlement not found")

    def get(self, request, pk):
        settlement = self.get_object(pk)
        serializer = SettlementSerializer(settlement)
        return Response(serializer.data)

    def put(self, request, pk):
        settlement = self.get_object(pk)
        serializer = SettlementSerializer(settlement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        raise CustomValidationError("Validation Error", serializer.errors)

    def delete(self, request, pk):
        settlement = self.get_object(pk)
        settlement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def SettlementSuggestion(request, pk):
    try:
        group = Group.objects.get(pk=pk)
    except Group.DoesNotExist:
        raise NotFoundError("Group not found")

    if not request.user.is_superuser and request.user not in group.members.all():
        raise InvalidInputError("You are not authorized to access suggestions for this group")

    suggestions = calculate_settlement_suggestions(group)
    return Response({
        "settlement_suggestions": suggestions
    }, status=status.HTTP_200_OK)