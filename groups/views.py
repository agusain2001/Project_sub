from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Group
from .serializers import GroupSerializer


class GroupListCreate(APIView):
      def get(self, request):
          groups = Group.objects.all()
          serializer = GroupSerializer(groups, many=True)
          return Response(serializer.data)

      def post(self, request):
          serializer = GroupSerializer(data=request.data)
          if serializer.is_valid():
              serializer.save()
              return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)