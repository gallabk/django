from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"newpost1app/home.html")

def add(request):
    
    val1 = int(request.POST["num1"]) 
    val2 = int(request.POST["num2"])

    res = val1 +val2 

    return render(request, "newpost1app/result.html", {"result" : res}) 