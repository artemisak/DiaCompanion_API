from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import DiaUsers
from .serializers import DiaUsersSerializer


# Create your views here.

@csrf_exempt
def get_all(request):
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
