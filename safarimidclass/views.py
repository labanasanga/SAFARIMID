from django.shortcuts import render
def homepage(request):
    return render(request,"index.html")
def aboutus(request):
    return render(request,"aboutus.html")