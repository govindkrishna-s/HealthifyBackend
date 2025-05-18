from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from api.serializers import UserCreationSerializer, MealSerializer
from rest_framework import authentication, permissions
from api.models import Meal
from api.permissions import IsOwnerPermissions
from rest_framework.views import APIView
from django.db.models import Sum
from rest_framework.response import Response

# Create your views here.

class SignUpView(CreateAPIView):
    serializer_class=UserCreationSerializer

class MealCreationView(CreateAPIView, ListAPIView):
    authentication_classes=[authentication.TokenAuthentication]
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
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[IsOwnerPermissions]


from django.utils import timezone
class MealSummaryView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request,*args,**kwargs):
        qs= Meal.objects.filter(owner=request.user,created_at__date=timezone.localdate())
        total_calorie=qs.values('calorie').aggregate(total=Sum('calorie'))
        meal_type_summary=qs.values('meal_type').annotate(total=Sum('calorie'))
        context={
            'calorie_total':total_calorie.get('total'),
            'meal_type_summary':meal_type_summary
        }
        return Response(data=context)