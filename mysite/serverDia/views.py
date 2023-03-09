from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

from .models import DiaUsers
from .serializers import DiaUsersSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def add_user(request):
    user_data = DiaUsersSerializer(data=request.data)
    print(user_data)
    if user_data.is_valid():
        user = DiaUsers.objects.create_user(user_data['username'].value)
        user.email = user_data['email'].value
        user.first_name = user_data['first_name'].value
        user.middle_name = user_data['middle_name'].value
        user.last_name = user_data['last_name'].value
        user.birth_date = user_data['birth_date'].value
        user.weight = user_data['weight'].value
        user.height = user_data['height'].value
        user.attending_doctor = user_data['attending_doctor'].value
        user.app_type = user_data['app_type'].value
        user.save()
        return Response(data=user_data.data, status=status.HTTP_201_CREATED)
    else:
        return Response(data=user_data.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request):
    snippets = DiaUsers.objects.all()
    serializer = DiaUsersSerializer(snippets, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user(request):
    pass


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request):
    pass


def home_page(request):
    return render(request, 'templates/home.html')
