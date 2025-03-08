from rest_framework import serializers
from .models import JobPosting  

# Serializer for creating a job (simpler version)
class CreateJobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting  # Use the JobPosting model
        fields = ['title', 'company', 'location', 'salary', 'description']  # Fields users can fill
        

# Serializer for showing all job details (fancy version)
class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = '__all__'  # Show ALL fields (including employer and created_at)
        read_only_fields = ('employer',)  # Don’t let users change the employer!