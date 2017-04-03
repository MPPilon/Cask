from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('userList.html')
    return HttpResponse(template.render(request))

def detail(request, user_id):
    return HttpResponse("<h2>User " + user_id + " details:")