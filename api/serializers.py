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