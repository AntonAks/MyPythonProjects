from django.http import HttpResponse
from django.shortcuts import render
from couter.tools import Text

def home(request):
    return render(request, 'home.html', {'key_1':'Hello again'})

def first_page(request):
    return render(request, 'first.html')

def second_page(request):
    return render(request, 'second.html')

def count_page(request):
    input_from_home_page = request.GET['input']
    word_list = str(input_from_home_page).split()

    text_data={'text':input_from_home_page,
               'words_number':word_list.__len__()}
    return render(request, 'count.html', context=text_data)

# TODO: need to read about render function
# TODO: need to read about request object
