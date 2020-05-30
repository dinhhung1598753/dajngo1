from django.shortcuts import render
from django.views import View
# Create your views here.

# func base view
# def index(request):
#     return render(request, 'index.html')

# class base view
class IndexView(View):

    def get(self,request):
        return render(request, 'index.html')

class Person(View):

    def get(self,request):
        text={
            'h1':'linh chi',
            'h2':'chi chi',
            'h3':['so1','so2'],

        }
        return render(request, 'index.html', text)