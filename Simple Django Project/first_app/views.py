from django.shortcuts import render
# from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord
from first_app.form import NewForm


# Create your views here.

def index(request):
    # Connecting models to views in the MTV paradigm
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}

    # my_dict = {'insert_me': 'Hello. I am from views.py!'}
    return render(request, 'first_app/index.html', context=date_dict)

def about(request):
    my_dict = {'insert_about': 'Hello. I am from views.py'}
    return render(request, 'first_app/about.html', context=my_dict)

def form_view(request):

    if request.method == 'POST':
         form = NewForm(request.POST)

         if form.is_valid():
             form.save(commit=True)
             return index(request)
         else:
              print('Form Invalid!')

    else:
         form = NewForm()

        #     print('Validation Success!')
        #     print('Name: '+form.cleaned_data['name'])
        #     print('Email: '+form.cleaned_data['email'])
        #     print('Text: '+form.cleaned_data['text'])

    return render(request, 'first_app/form.html', {'form':form})
