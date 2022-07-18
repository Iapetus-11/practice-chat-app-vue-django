from datetime import datetime
import json
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
import django.middleware.csrf

from .models import Message

# Create your views here.


def get_messages(request: HttpRequest):
    return JsonResponse(list(Message.objects.order_by("created_at").all().values("id", "user_name", "content", "created_at")), safe=False)


def create_message(request: HttpRequest):
    data = json.loads(request.body)

    user_name = data["msg_user_name"]
    user_ip = request.headers.get("CF-Connecting-Ip", request.headers.get("X-Forwarded-For", request.META.get("REMOTE_ADDR")))
    content = data["msg_content"]
    created_at = datetime.utcnow()

    Message(user_name=user_name, user_ip=user_ip, content=content, created_at=created_at).save()

    return HttpResponse("200 success!")
