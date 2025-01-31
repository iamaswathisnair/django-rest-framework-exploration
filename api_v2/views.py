from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Teacher
from .serializers import TeacherSerializer


@api_view(['GET', 'POST'])
def teacher_list(request):
    if request.method == 'GET':  # If GET request
        Teachers = Teacher.objects.all()
        serializer = TeacherSerializer(Teachers, many=True)
#The key reason you serialize again is that Django models like Teacher are Python objects, but when you return them as part of an API response, they need to be in a JSON format.
        return Response(serializer.data)


    elif request.method == 'POST':  # If POST request
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save data to the database
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)




    
    