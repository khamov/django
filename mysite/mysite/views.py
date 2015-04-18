from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello, Alex!")

def cur_date(request):
    now = datetime.datetime.now()
    html = "<html><body>Now is %s.</body></html>"%now
    return HttpResponse(html)

def hour_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
    assert False
    html = "<html><body>After %s hours will be %s.</body></html>"%(offset,dt)
    
    return HttpResponse(html)
