from django.urls import path
from api import views

urlpatterns=[
    path('register/',views.SignUpView.as_view()),
    path('meal/',views.MealCreationView.as_view()),
    path('meal/<int:pk>/',views.MealDetailView.as_view())
]