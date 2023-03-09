from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import DiaUsers
from .serializers import DiaUsersSerializer

@api_view(['POST'])
def add_user(request):
    user_data = DiaUsersSerializer(data=request.data)
    if user_data.is_valid():
        DiaUsers.objects.create_user(user_data['username'].value)
        DiaUsers.email = user_data['email'].value
        DiaUsers.first_name = user_data['first_name'].value
        DiaUsers.middle_name = user_data['middle_name'].value
        DiaUsers.last_name = user_data['last_name'].value
        DiaUsers.birth_date = user_data['birth_date'].value
        DiaUsers.weight = user_data['weight'].value
        DiaUsers.height = user_data['height'].value
        DiaUsers.attending_doctor = user_data['attending_doctor'].value
        DiaUsers.app_type = user_data['app_type'].value
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
