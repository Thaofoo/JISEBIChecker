from django.shortcuts import render

def upload(request):
    return render(request, 'manuscripts/upload.html')

def report(request):
    return render(request, "manuscripts/report.html")

def full_report(request):
    return render(request, "manuscripts/full_report.html")


