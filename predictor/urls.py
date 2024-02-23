# predictor/urls.py
from django.urls import path
from .views import predict_kidney_disease

urlpatterns = [
    path('predict/', predict_kidney_disease, name='predict_kidney_disease'),
]

