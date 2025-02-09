from django.shortcuts import render
from . models import Student
from . serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json

# Create your views here.

def student_details(request):
    stu = Student.objects.get(id=1)
    serializer = StudentSerializer(stu)   #Serializing the Student Object , Serializers convert Python objects into dictionary format, which is closer to JSON.
    json_data = JSONRenderer().render(serializer.data) #SONRenderer converts the dictionary into a JSON string.
    return HttpResponse(json_data , content_type ='application/json') #Sends the JSON string to the client. The content_type='application/json' tells the client (like a browser or app) that the response contains JSON data.
# Use httpresponse When manually setting the response type (content_type="text/html" or content_type="application/json")
# Httpresponse By default, it sends HTML, but we can make it send JSON by specifying content_type='application/json'.

def hello_world(request):
    data = {"message": "Hello, world!"}
    json_data = json.dumps(data)  # Convert Python dictionary to JSON string
    return HttpResponse(json_data, content_type="application/json")


#above same concept using jsonrespinse 

def hello_world(request):
    return JsonResponse({"message": "Hello, world!"})

#for getting all data 

def all_student(request):
    # Fetch all students from the database
    data = Student.objects.all()
    
    # Serialize the data (convert to JSON-like structure)
    serializer = StudentSerializer(data, many=True)
    
    # Return the serialized data as JSON response
    return JsonResponse(serializer.data, safe=False)

# safe=True: Only dictionaries are allowed. This is safer and follows typical JSON response practices.
# safe=False: Allows returning non-dictionaries. Use it carefully, especially if the client expects a specific data format.
# Handles safe=True by default, preventing errors when returning non-dictionary data.If you want to return a list, you must use safe=False:





                                    # crud operations using fbv

# Retrieve All Students or a Single Student

@api_view(['GET'])
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()  # Fetch all student records
        serializer = StudentSerializer(students, many=True)  # Serialize multiple objects
        return Response(serializer.data)  # Return JSON response
   
    
# For a single student:

@api_view(['GET'])
def student_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)  # Fetch student by primary key (id)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = StudentSerializer(student)  # Serialize a single object
    return Response(serializer.data)  # Return JSON response


# Create a New Student

@api_view(['POST'])
def student_create(request):
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)  # Deserialize incoming JSON
        if serializer.is_valid():  # Validate data
            student = Student.objects.create(**serializer.validated_data)  # Save to DB
            return Response(StudentSerializer(student).data, status=status.HTTP_201_CREATED)  # Return saved data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors if invalid
    
    
    

# Update an Existing Student
@api_view(['PUT'])
def student_update(request, pk):
    try:
        student = Student.objects.get(pk=pk)  # Fetch student by primary key
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)  # Deserialize JSON and include existing data
        if serializer.is_valid():
            student.name = serializer.validated_data['name']
            student.roll = serializer.validated_data['roll']
            student.city = serializer.validated_data['city']
            student.save()  # Save updated data to the database
            return Response(serializer.data)  # Return updated student data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors if invalid



# Partially Update an Existing Student (Partial Update)

@api_view(['PATCH'])
def student_partial_update(request, pk):
    try:
        student = Student.objects.get(pk=pk)  # Fetch student by primary key
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        serializer = StudentSerializer(student, data=request.data, partial=True)  # Allow partial updates
        if serializer.is_valid():
            serializer.save()  # Save the changes to the database
            return Response(serializer.data)  # Return updated student data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors if invalid
    

# Delete a Student

@api_view(['DELETE'])
def student_delete(request, pk):
    try:
        student = Student.objects.get(pk=pk)  # Fetch student by primary key
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        student.delete()  # Delete the student from the database
        return Response({'message': 'Student deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
