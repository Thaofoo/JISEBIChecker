from django.shortcuts import render

def uploadView(request):
    return render(request, 'uploadIndex.html')

def full_report(request):
    return render(request, "full_report.html")

