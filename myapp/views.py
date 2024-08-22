from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

# def home(request):
#     return HttpResponse("Hello, welcome to my website!")

def home(request):
    return render(request, 'index.html')


def admin_dashboard(request):
    return render(request, 'admin/dashboard/dashboard.html')