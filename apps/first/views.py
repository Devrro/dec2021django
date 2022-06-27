import json

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class ComputerView(APIView):
    def get(self, *args, **kwargs):
        return Response('Method GET')

    def post(self, *args, **kwargs):
        return Response('Method POST')

    def put(self, *args, **kwargs):
        return Response('Method PUT')

    def delete(self, *args, **kwargs):
        return Response('Method DELETE')

    def patch(self, *args, **kwargs):
        return Response('Method PATCH')

