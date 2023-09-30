from django.shortcuts import render

def uploadView(request):
    return render(request, 'uploadIndex.html')
