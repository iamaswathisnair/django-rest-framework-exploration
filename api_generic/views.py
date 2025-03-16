# GenericApiView and model mixins

from django.shortcuts import render
from . models import Restaurant
from . serializers import RestaurantSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin , CreateModelMixin , UpdateModelMixin , RetrieveModelMixin , DestroyModelMixin

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
class RestaurantListCreateAPI(GenericAPIView ,ListModelMixin , CreateModelMixin):
    queryset = Restaurant.objects.all()  # 1. Fetch all restaurants
    serializer_class = RestaurantSerializer  # 2. Convert to JSON
    authentication_classes = [TokenAuthentication]  # ✅ Token-based authentication (Per View)
    permission_classes = [IsAuthenticated]  # ✅ Restrict access to authenticated users

    def get(self, request):
        return self.list(request)  # ✅ Handles GET request (List all restaurants)

    def post(self, request):
        return self.create(request)  # ✅ Handles POST request (Create a restaurant)
    



# ------------------------------------------------------------------------------------------------------



class RestaurantDetailAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Restaurant.objects.all()  # Fetch all restaurants
    serializer_class = RestaurantSerializer  # Convert to JSON
    authentication_classes = [TokenAuthentication]  # ✅ Token-based authentication (Per View)
    permission_classes = [IsAuthenticated]  # ✅ Restrict access to authenticated users



    def get(self, request, pk):
        return self.retrieve(request, pk)  # ✅ Handles GET request (Fetch one restaurant)

    def put(self, request, pk):
        return self.update(request, pk)  # ✅ Handles PUT request (Update restaurant)

    def delete(self, request, pk):
        return self.destroy(request, pk)  # ✅ Handles DELETE request (Delete restaurant)
    
    
    
    
    
# class RestaurantDetailAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, PartialUpdateModelMixin):
#     queryset = Restaurant.objects.all()
#     serializer_class = RestaurantSerializer

#     def get(self, request, pk):
#         return self.retrieve(request, pk)

#     def put(self, request, pk):
#         return self.update(request, pk)  # ✅ Full Update

#     def patch(self, request, pk):
#         return self.partial_update(request, pk)  # ✅ Partial Update

#     def delete(self, request, pk):
#         return self.destroy(request, pk)