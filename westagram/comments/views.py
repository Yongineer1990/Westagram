import json
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from users.models import Users
from .models import Comments

# Create your views here.


class Write (View):
    def post(self, request):
        data = json.loads(request.body)
        Comments(
            user_account=Users.objects.get(name=data["name"]),
            comment_text=data["text"],
        ).save()

        return JsonResponse({"message": "SUCCESS"}, status=200)

    def get(self, request):
        comment_data = Comments.objects.values()
        return JsonResponse({"commnets": list(comment_data)}, status=200)


class Update (View):
    def post(self, request):
        data = json.loads(request.body)

        update_content = Comments.objects.get(id=data["id"])
        update_content.comment_text = data["text"]
        update_content.save()

        return JsonResponse({"message": "SUCCESS"}, status=200)
