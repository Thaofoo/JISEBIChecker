from django.shortcuts import render

def uploadView(request):
    context = {'message': 'Halo, ini pesan dari view kustom!'}
    return render(request, 'uploadIndex.html', context)
