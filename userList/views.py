from django.http import HttpResponse
from django.template import loader
from rest_framework import generics

from userList.models import User
from userList.serializers import UserSerializer


class ListCreateUsers(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def index(request):
    template = loader.get_template('userList.html')
    return HttpResponse(template.render(request))

def detail(request, user_id):
    return HttpResponse("<h2>User " + user_id + " details:")