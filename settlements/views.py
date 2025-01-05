from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Settlement
from .serializers import SettlementSerializer


class SettlementListCreate(APIView):
      def get(self, request):
          settlements = Settlement.objects.all()
          serializer = SettlementSerializer(settlements, many=True)
          return Response(serializer.data)

      def post(self, request):
          serializer = SettlementSerializer(data=request.data)
          if serializer.is_valid():
              serializer.save()
              return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)