from django.shortcuts import render
from . models import Student
from . serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework.parsers import JSONParser

# Create your views here.

def student_details(request):
    stu = Student.objects.get(id=1)
    serializer = StudentSerializer(stu)   #Serializing the Student Object , Serializers convert Python objects into dictionary format, which is closer to JSON.
    json_data = JSONRenderer().render(serializer.data) #SONRenderer converts the dictionary into a JSON string.
    return HttpResponse(json_data , content_type ='application/json') #Sends the JSON string to the client. The content_type='application/json' tells the client (like a browser or app) that the response contains JSON data.

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



def create_student(request):
    if request.method == 'POST':
        
        # Deserialize the incoming JSON data
        data = JSONParser().parse(request)  # Convert the incoming JSON into a Python dictionary
        
        
        # Use the serializer to check and validate the data
        serializer = StudentSerializer(data=data)

        if serializer.is_valid():  # Check if the data is valid according to the model fields
            serializer.save()  # Save the new student to the database
            return JsonResponse(serializer.data, status=201)  # Return the serialized data of the newly created student
        return JsonResponse(serializer.errors, status=400)  # If data is invalid, return errors