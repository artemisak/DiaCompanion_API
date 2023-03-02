from http import HTTPStatus

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import DiaUsers
from .serializers import DiaUsersSerializer

# fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'middle_name',
#           'birth_date', 'weight', 'height', 'attending_doctor', 'app_type', 'last_login', 'is_superuser',
#           'is_staff', 'is_active', 'date_joined']
@api_view(['POST'])
def addUser(request):
    user_data = DiaUsersSerializer(data=request.data)
    if user_data.is_valid():
        DiaUsers.objects.create_user(user_data['username'].value)
        return Response(data=user_data.data, status=status.HTTP_201_CREATED)
    else:
        return Response(data=user_data.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUser(request):
    snippets = DiaUsers.objects.all()
    serializer = DiaUsersSerializer(snippets, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUser(request):
    pass


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteUser(request):
    pass


def home_page(request):
    return render(request, 'templates/home.html')
