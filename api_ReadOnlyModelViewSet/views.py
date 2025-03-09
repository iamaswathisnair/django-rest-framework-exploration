from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Restaurant
from .serializers import RestaurantSerializer




class RestaurantViewSet(ReadOnlyModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    
    
    
    
# filtering code


# If no query parameter is provided:
# It returns all data (full data).
# If a query parameter (like company) is provided:
# It returns the filtered data.



# class JobPostingReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
#     serializer_class = JobPostingSerializer

#     def get_queryset(self):
#         # Start with all job postings
#         queryset = JobPosting.objects.all()
#         # Check if a "company" parameter is provided in the URL query string
#         company = self.request.query_params.get('company')
#         if company:
#             # If the parameter exists, filter the queryset by company name (case-insensitive)
#             queryset = queryset.filter(company__iexact=company)
#         # If no company parameter, the full queryset is returned
#         return queryset