from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'npm' : '2306165641',
        'name': 'Alya Rasheeda Yuvana',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
