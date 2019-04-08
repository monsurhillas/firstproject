from django.http import HttpResponse
import datetime

def index(request):
    now = datetime.datetime.now()
    html = "<h1> hello the current time is %s </h1>" %now
    return  HttpResponse(html)
