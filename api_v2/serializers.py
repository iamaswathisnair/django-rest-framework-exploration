from rest_framework import serializers
from . models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Teacher
        fields = "__all__"
        # exclude = ['age']  # Everything except 'age'
        
    
    
#another way arguments passing readonly     
class TeacherSerializer(serializers.ModelSerializer):
    name=serializers.CharField(read_only =True)
    class Meta:
        Model = Teacher
        # fields = "__all__"
        fields = ['id', 'name', 'roll', 'city']
        read_only_fields =['name' , 'age']
        
        
#custome validation in creete()        
# def create(self, validated_data):
#         validated_data['password'] = hash_function(validated_data['password'])  # Hash password
#         return super().create(validated_data)