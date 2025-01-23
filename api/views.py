from django.shortcuts import render
from . models import Student
from . serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.

def student_details(request):
    stu = Student.objects.get(id=1)
    serializer = StudentSerializer(stu)   #Serializing the Student Object , Serializers convert Python objects into dictionary format, which is closer to JSON.
    json_data = JSONRenderer().render(serializer.data) #SONRenderer converts the dictionary into a JSON string.
    return HttpResponse(json_data , content_type ='application/json') #Sends the JSON string to the client.