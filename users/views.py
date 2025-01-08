from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from utils.custom_errors import NotFoundError, CustomValidationError
from utils.permissions import IsAdminOrReadOnly
from utils.helpers import paginate_response


class UserListCreate(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        users = User.objects.all()
        return paginate_response(users, request, UserSerializer)

    def post(self, request):
         serializer = UserSerializer(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
         raise CustomValidationError("Validation Error", serializer.errors)


class UserDetail(APIView):
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFoundError("User not found")

    def get(self, request, pk):
         user = self.get_object(pk)
         serializer = UserSerializer(user)
         return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
        raise CustomValidationError("Validation Error", serializer.errors)


    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TokenAPI(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username).first()
        if user is None or not user.check_password(password):
            return Response({"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })