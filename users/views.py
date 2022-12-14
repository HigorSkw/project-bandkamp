# from rest_framework.views import APIView, Request, Response, status
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer

# from django.shortcuts import get_object_or_404
from .permissions import IsAccountOwner

# from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# class UserView(APIView):
#     def post(self, request: Request) -> Response:
#         """
#         Registro de usuários
#         """
#         serializer = UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         serializer.save()

#         return Response(serializer.data, status.HTTP_201_CREATED)

#     def get(self, request:Request) -> Response:
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)

#         return Response(serializer.data, status.HTTP_200_OK)

# class UserView(CreateAPIView, ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class UserDetailView(APIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAccountOwner]

#     def get(self, request: Request, pk: int) -> Response:
#         """
#         Obtençao de usuário
#         """
#         user = get_object_or_404(User, pk=pk)

#         serializer = UserSerializer(user)

#         return Response(serializer.data)

#     def patch(self, request: Request, pk: int) -> Response:
#         """
#         Atualização de usuário
#         """
#         user = get_object_or_404(User, pk=pk)

#         serializer = UserSerializer(user, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(serializer.data)

#     def delete(self, request: Request, pk: int) -> Response:
#         """
#         Deleçao de usuário
#         """
#         user = get_object_or_404(User, pk=pk)

#         user.delete()

#         return Response(status=status.HTTP_204_NO_CONTENT)

# class UserDetailView(RetrieveAPIView, DestroyAPIView, UpdateAPIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAccountOwner]

#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer
