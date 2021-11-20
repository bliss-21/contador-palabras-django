from django.shortcuts import render

# Create your views here.
def home(request):

    data = {}

    if request.POST:
        texto =  request.POST.get('texto')
        data['mensaje'] = len(texto)

    return render(request, 'core/home.html', data)