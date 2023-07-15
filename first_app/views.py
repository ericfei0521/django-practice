from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecords, WebPage

# Create your views here.


def index(request):
    webList = AccessRecords.objects.order_by("date")
    response = []
    for list in webList:
        returnList = {"name": list.name, "date": list.date}
        web = WebPage.objects.filter(name=list.name)[0]
        returnList["url"] = web.url
        response.append(returnList)
    response = {"records": response}
    return render(request, "first_app/index.html", context=response)
