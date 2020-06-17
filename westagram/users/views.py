import json
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse
from .models import Users
import bcrypt
import jwt

# Create your views here.


class SignUp (View):
    def post(self, request):
        data = json.loads(request.body)
        hashed_password = bcrypt.hashpw(
            data["password"].encode('utf-8'), bcrypt.gensalt())
        Users(
            name=data["name"],
            email=data["email"],
            password=hashed_password
        ).save
        return JsonResponse({"message": "SUCCESS"}, status=200)


class Login (View):
    def post(self, request):
        data = json.loads(request.body)
        if Users.objects.filter(email=data["email"]).exists():
            user = Users.objects.get(email=data["email"])
            if bcrypt.checkpw(data["password"].encode('utf-8'), user.password):
                encoded_jwt = jwt.encode(
                    {"user": data["email"]}, 'secret', algorithm='HS256')
                decoded_jwt = jwt.decode(
                    encoded_jwt, 'secret', algorithms='HS256')
                return JsonResponse({"message": "Login Success", "jwt": decoded_jwt}, status=200)
            else:
                return JsonResponse({"message": "INVALID_USER"}, status=401)
        else:
            return JsonResponse({"message": "INVALID_USER"}, status=401)
