from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Teacher
from .serializers import TeacherSerializer




                    #Handles listing all teachers and creating a new teacher.

@api_view(['GET', 'POST'])    
def teacher_list(request):
    if request.method == 'GET':  # If GET request
        Teachers = Teacher.objects.all()
        serializer = TeacherSerializer(Teachers, many=True)
#The key reason you serialize again is that Django models like Teacher are Python objects,
#but when you return them as part of an API response, they need to be in a JSON format.
# Django models store data as Python objects.
# To send this data as an API response, it must be converted to JSON.
# Serializers handle this conversion, so the frontend or API consumer can understand the response
        return Response(serializer.data)


    elif request.method == 'POST':  # If POST request
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save data to the database
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# Get a Single Teacher by ID

@api_view(['GET'])
def get_teacher_by_id(request, pk):
    try:
        teacher = Teacher.objects.get(pk=pk)
    except Teacher.DoesNotExist:
        return Response({'error': 'Teacher not found'}, status=404)

    serializer = TeacherSerializer(teacher)
    return Response(serializer.data)  



#Update a Teacher

@api_view(['PUT'])  #This function ONLY allows PUT, so no need to check method if req.mehotd
def update_teacher(request, pk):
    try:
        teacher = Teacher.objects.get(pk=pk) #✅ Getting teacher
    except Teacher.DoesNotExist:
        return Response({'error': 'Teacher not found'}, status=404)

    serializer = TeacherSerializer(teacher, data=request.data)  # Step 3: Pass existing teacher + new data
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


# Delete a Teacher

@api_view(['DELETE'])
def delete_teacher(request, pk):
    try:
        teacher = Teacher.objects.get(pk=pk)
    except Teacher.DoesNotExist:
        return Response({'error': 'Teacher not found'}, status=404)

    teacher.delete()
    return Response({'message': 'Teacher deleted successfully'}, status=204)