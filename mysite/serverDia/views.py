from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from rest_framework.parsers import JSONParser
from .models import DiaUsers
from .serializers import DiaUsersSerializer


@login_required
def get_all_users(request):
    if request.method == 'GET':
        snippets = DiaUsers.objects.all()
        serializer = DiaUsersSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DiaUsersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def user_login(request):
    if request.method == 'GET':
        csrf_token = get_token(request)
        #csrf_token_html = '<input type="hidden" name="csrfmiddlewaretoken" value="{}" />'.format(csrf_token)
        return HttpResponse(csrf_token)
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=403)


def home_page(request):
    return render(request, 'templates/home.html')
