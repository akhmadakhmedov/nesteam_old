from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserListSerializer, UserSerializer
from rest_framework.viewsets import ModelViewSet
from django.http import JsonResponse

def users_list(request):
    users = User.objects.all()
    serializer = UserListSerializer(users, many=True)
    data = serializer.data
    return JsonResponse(data, safe=False)

def user_detail(request, pk):
    user_object = User.objects.get(pk=pk)
    serializer = UserListSerializer(user_object)
    return JsonResponse(serializer.data, safe=False)

class UserViewSet(ModelViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
