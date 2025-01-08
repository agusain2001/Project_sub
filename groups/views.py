from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .models import Group
from .serializers import GroupSerializer
from utils.permissions import IsOwnerOrAdminOrReadOnly
from utils.custom_errors import NotFoundError, CustomValidationError
from utils.helpers import paginate_response


class GroupListCreate(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        groups = Group.objects.all()
        return paginate_response(groups, request, GroupSerializer)


    def post(self, request):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        raise CustomValidationError("Validation Error", serializer.errors)


class GroupDetail(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdminOrReadOnly]

    def get_object(self, pk):
        try:
            return Group.objects.get(pk=pk)
        except Group.DoesNotExist:
             raise NotFoundError("Group not found")


    def get(self, request, pk):
         group = self.get_object(pk)
         serializer = GroupSerializer(group)
         return Response(serializer.data)

    def put(self, request, pk):
        group = self.get_object(pk)
        serializer = GroupSerializer(group, data=request.data)
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
        raise CustomValidationError("Validation Error", serializer.errors)


    def delete(self, request, pk):
         group = self.get_object(pk)
         group.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)