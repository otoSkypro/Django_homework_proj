from django.shortcuts import render


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST('message')
        print(f'Ваше имя {name}, Контактный телефон {phone}, Введите текст {message}')
    return render(request, 'catalog/contacts.html')



