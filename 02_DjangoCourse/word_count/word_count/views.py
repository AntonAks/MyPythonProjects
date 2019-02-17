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
    text_object = Text(input_from_home_page)

    text_data={'text':text_object.content,
               'words_number':text_object.number_of_words,
               'words_number_unique':text_object.number_of_unique_words,
               'words_dict':text_object.words}

    return render(request, 'count.html', context=text_data)

# TODO: need to read about render function
# TODO: need to read about request object
