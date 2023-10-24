from django.shortcuts import render
from .modules.CompanyInfo import CompanyInfo

company:dict = {"company": CompanyInfo().__dict__}

responseData = {k:v for k,v in company.items()}

responseData.update({
    "developers": [
        "Abel Akponine"
    ],
    "AppName": "Pekaboom Enterprise Limited"
})

print(responseData["AppName"])


# Create your views here.
def welcome(request):
    return render(request, "index.html", responseData)