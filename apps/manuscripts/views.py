from django.shortcuts import render

def upload(request):
    return render(request, 'upload.html')

def full_report(request):
    return render(request, "full_report.html")

