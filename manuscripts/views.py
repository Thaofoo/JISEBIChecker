from django.shortcuts import render

# Create your views here.
def full_report(request):
    return render(request, "full_report.html")
