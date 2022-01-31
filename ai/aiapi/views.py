import requests
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView


class Predict(APIView):
    def post(self, request):
        url = 'http://194.59.40.131:8081/v1/models/melanomaapp:predict'
        payload = str(request.data).replace("'", "\"")

        r = requests.post(url, data=payload)
        return Response(r.json())
