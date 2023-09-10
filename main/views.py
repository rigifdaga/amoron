from django.shortcuts import render

def show_main(request):
    context = {
        'app': 'Amoron Rental',
        'nama': 'Rifda Aulia Nurbahri',
        'kelas' : 'PBP D'
    }

    return render(request, "main.html", context)