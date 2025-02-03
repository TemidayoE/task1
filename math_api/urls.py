from django.urls import path
from math_api.views import classify_number

urlpatterns = [
    path('classify-number/', classify_number, name= "classify-number")
]
