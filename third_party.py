import requests

def check_api_status(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            print("API is working correctly!")
            print("Response Data:", response.json())  # you make a request to an API and get back a JSON response ,and convert that JSON data from the response into Python objects
        else:
            print(f"API returned an error. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print("Error while checking the API:", e)

# Replace with your actual API URL
api_url = "http://127.0.0.1:8000/all_student/"
check_api_status(api_url)




#CRUD CODE 

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer

# READ (Retrieve all tasks or a single task)
@api_view(['GET'])
def task_list(request):
    if request.method == 'GET':
        tasks = Task.objects.all()  # Fetch all tasks
        serializer = TaskSerializer(tasks, many=True)  # Serialize multiple tasks
        return Response(serializer.data)  # Send serialized data as JSON


# CREATE a new task
@api_view(['POST'])
def task_create(request):
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)  # Deserialize incoming JSON
        if serializer.is_valid():  # Validate data
            serializer.save()  # Save to database
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Success response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Error response


# UPDATE an existing task
@api_view(['PUT'])
def task_update(request, pk):
    try:
        task = Task.objects.get(pk=pk)  # Get task by primary key
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)  # Deserialize incoming JSON
        if serializer.is_valid():  # Validate data
            serializer.save()  # Save updated data
            return Response(serializer.data)  # Success response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Error response


# DELETE a task
@api_view(['DELETE'])
def task_delete(request, pk):
    try:
        task = Task.objects.get(pk=pk)  # Get task by primary key
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        task.delete()  # Delete the task
        return Response({'message': 'Task deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
