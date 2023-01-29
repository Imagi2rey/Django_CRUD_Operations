from django.urls import path  
from . import views

urlpatterns = [
	path('fruits/', views.FruitList.as_view()),
	path('fruits/<int:id>/', views.FruitDetail.as_view(), name='fruit-detail'),
]