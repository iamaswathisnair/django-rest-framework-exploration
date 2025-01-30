from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
     name =serializers.CharField(max_length=100)
     roll =serializers.IntegerField()
     city =serializers.CharField(max_length=100)
# in model id is autogebrated but when ouput load its not show so when you want to see id you need to explicity mention tat in serailizer 
     id =serializers.IntegerField()
     
     
# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = ['id', 'name', 'age', 'email']




"""another eg"""

# from rest_framework import serializers
# from .models import Student

# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     age = serializers.IntegerField()
#     grade = serializers.CharField(max_length=5)

    # Create method for saving new objects
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

    # Update method for modifying existing objects
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.age = validated_data.get('age', instance.age)
#         instance.grade = validated_data.get('grade', instance.grade)
#         instance.save()
#         return instance


""" views """

# @api_view(['POST'])
# def create_student(request):
#     serializer = StudentSerializer(data=request.data)  
#     if serializer.is_valid():
#         serializer.save()  # This calls create() method
#         return Response(serializer.data, status=201)
#     return Response(serializer.errors, status=400)

# @api_view(['PUT'])
# def update_student(request, pk):
#     student = Student.objects.get(id=pk)  # Get the existing student
#     serializer = StudentSerializer(student, data=request.data)  
#     if serializer.is_valid():
#         serializer.save()  # This calls update() method
#         return Response(serializer.data)
#     return Response(serializer.errors, status=400)
