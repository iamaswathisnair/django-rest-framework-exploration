from rest_framework import serializers
from  models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Teacher
        fields = "__all__"
        # exclude = ['age']  # Everything except 'age'