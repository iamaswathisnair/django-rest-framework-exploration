
from rest_framework import viewsets
from .models import JobPosting
from .serializers import JobPostingSerializer, CreateJobPostingSerializer
from rest_framework.permissions import IsAuthenticated  # Only logged-in users can play!

class JobPostingViewSet(viewsets.ModelViewSet):
    queryset = JobPosting.objects.all()  # "Grab all jobs from the database"
    permission_classes = [IsAuthenticated]  # You must be logged in to use this!

    # Choose the right serializer for the action
    def get_serializer_class(self):
        if self.action == 'create':  # If creating a job, use the simple serializer
            return CreateJobPostingSerializer
        return JobPostingSerializer  # Otherwise, use the fancy one

    # Automatically set the employer when creating a job
    def perform_create(self, serializer):
        serializer.save(employer=self.request.user)  # "The employer is YOU!"