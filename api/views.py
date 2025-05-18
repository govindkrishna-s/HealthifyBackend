from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from api.serializers import UserCreationSerializer, MealSerializer
from rest_framework import authentication, permissions
from api.models import Meal
from api.permissions import IsOwnerPermissions

# Create your views here.

class SignUpView(CreateAPIView):
    serializer_class=UserCreationSerializer

class MealCreationView(CreateAPIView, ListAPIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=MealSerializer
    queryset=Meal.objects.all()
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    def get_queryset(self):
        return self.request.user.meals.all()
    
class MealDetailView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    serializer_class=MealSerializer
    queryset=Meal.objects.all()
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[IsOwnerPermissions]
