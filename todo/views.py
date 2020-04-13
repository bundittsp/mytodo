from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .serializers import ToDoItemSerializer
from .models import ToDoItem

# Create your views here.
def index(request):
    return render(request, 'todo.html')


@csrf_exempt
@api_view(['GET', 'POST'])
def listcreate_api(request):
    """
    List all todo items, or create a new todo item.
    """
    if request.method == 'GET':
        items = ToDoItem.objects.all()
        serializer = ToDoItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ToDoItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)