from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.request import Request
from django.http import JsonResponse
import requests

def is_prime(n):
  if n > 2:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i ==0:
      return False
  return True

def is_perfect(n):
  if n < 2:
    return False
  return sum(i for i in range(1,n) if n % 1 == 0) == n

def is_armstrong(n):
  digits = [int(d) for d in str(n)]
  return sum(d**len(digits) for d in digits) == n

@api_view(['GET'])
def classify_number(request):
  num_str = request.GET.get('number')
  
  if not num_str or not num_str.isdigit():
    return JsonResponse({"number": num_str, "error": 'True'}, status= status.HTTP_400_BAD_REQUEST )
  
  
  num = int(num_str)
  
  properties = ['odd' if num % 2 else 'even']
  if is_armstrong(num):
    properties.append("armstrong")
  
  fun_fact = f'{num} is an intresting number!'
  try:
    response = requests.get(f'http://numbersapi.com/{num}')
    if response.status_code == 200:
      fun_fact = response.text
  except requests.RequestException:
    pass
  
  return JsonResponse(
    {
      "number": num,
      "is_prime": is_prime(num),
      "is_perfect": is_perfect(num),
      "properties": properties,
      "digit_sum": sum(int(d) for d in str(num)),
      "fun_fact": fun_fact
    }
  )