from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import User
from django.core import serializers


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
def users(request):
    users = User.objects.all()
    user_list = serializers.serialize('json',users)
    return HttpResponse(user_list, content_type="text/json-comment-filtered")
