from django.shortcuts import render
from django.views.generic import ListView, View
from .models import Home
import pyodbc
import re

def home(request):
    return render(request,'home.html',{})

class HomeView(ListView):
    model = Home
    template_name = 'home.html'

class HadisDeryasiView(View):

    def __init__(self):
        self.arabic_pattern = "[\u0600-\u06FF]+"

    def remove_diacritics(self, text):
        # Harekeleri kaldırmak için bir regex deseni
        diacritics_pattern = re.compile("[\u064b-\u0652\u0640]")

        # Harekeleri kaldır
        cleaned_text = re.sub(diacritics_pattern, "", text)

        return cleaned_text

    def get(self, request, *args, **kwargs):

        query = request.GET.get('query')
        hadis = request.GET.get('hadis')
        hadis_file = str(hadis)
        
        if query:
            #query = self.remove_diacritics(query) //harekeli aramayı harekesizleştirir.
            with open(f'texts/{hadis_file}.txt', 'r', encoding="utf-8") as file:
                paragraphs = file.read().split('**')  # Paragrafları * işaretine göre ayır
            liste = []
            for paragraph in paragraphs:
                if (query in paragraph) or (query in self.remove_diacritics(paragraph)):
                    liste.append(paragraph)
           # Bulunan paragrafı ekrana 
            return render(request, 'hadis_menu.html', {'kelime': query, "search_result": liste, 'selected_hadis': hadis,})
        else:
            return render(request, 'hadis_menu.html', {"search_result": [],})
    
    
class SqlServerConnView(View):
    def get(self, request):
        conn = pyodbc.connect('Driver={sql server};'
                              'Server=LAPTOP-R60FAUB3\SQLEXPRESS;'
                              'Database=LugatDB;'
                              'Trusted_connection=yes')
        cursor = conn.cursor()
        cursor.execute("select top 100 * from osmanlica")
        result = cursor.fetchall()
        return render(request, 'lugat.html', {'Sqlserverconn': result})
