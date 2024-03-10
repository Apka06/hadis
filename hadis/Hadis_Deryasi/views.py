from django.shortcuts import render
from django.views.generic import ListView, View
from .models import Home, FavoritesWord, FavoritesHadis
from django.shortcuts import redirect
from django.http import JsonResponse
import pyodbc
import re
import langdetect

def home(request):
    return render(request,'home.html',{})

class HomeView(ListView):
    model = Home
    template_name = 'home.html'

class HadisDeryasiView(View):

    def __init__(self):
        self.arabic_pattern = "[\u0600-\u06FF]+"
        self.star = "**"
        self.underscore = "__________"
        self.closing = ")"
        self.seperator = {"buhari":self.star,
                          "nesai":self.star,
                          "muslim":self.star,
                          "ebudavud":self.underscore,
                          "tirmizi":self.underscore,
                          "ibnmace":self.underscore,
                          "ibnhibban":self.underscore,
                          "muvattamhmd":self.closing,
                          "muvattamusab":self.closing,
                          "musnedahmed":self.closing,}

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
            with open(f'texts/hadis/{hadis_file}.txt', 'r', encoding="utf-8") as file:
                paragraphs = file.read().split(self.seperator[hadis_file])  # Hadisleri kitabın kendi ayıracına göre ayırır.
            result = []
            for paragraph in paragraphs:
                if (query in paragraph) or (query in self.remove_diacritics(paragraph)):
                    paragraph = paragraph.replace(self.underscore, "")
                    result.append(paragraph)
            return render(request, 'hadis_menu.html', {'kelime': query, "search_result": result, 'selected_hadis': hadis,})
        else:
            return render(request, 'hadis_menu.html', {"search_result": [],})
    
    def post(self, request):

        favori_content = request.POST.get('content')
        favori_book = request.POST.get('book')

        if not FavoritesHadis.objects.filter(content=favori_content, book=favori_book, owner=request.user).exists():
            FavoritesHadis.objects.create(
                number=1,  
                content=''.join(str(favori_content)),      
                book=str(favori_book),   
                owner=request.user
            )
            return JsonResponse({'exists': False})
        else:
            return JsonResponse({'exists': True})
    
    
class SqlServerConnView(View):
    
    def is_arabic(self, text):
        return (langdetect.detect(text) == "ar")
    
    def connect_database(self, query):

        print("database")

        with open("Hadis_Deryasi/database.txt", "r") as file:
            database = file.readline()
            print(database)

        conn = pyodbc.connect('Driver={sql server};'
                              f'Server={database};'
                              'Database=LugatDB;'
                              'Trusted_connection=yes')
        cursor = conn.cursor()

        length = len(str(query))
        
        if not self.is_arabic(query):
            if length == 1:
                cursor.execute("select kid,onay,diger,isim,diger2,koku,kelime from osmanlica where isim like '" + str(query) + "%'")
            else:
                cursor.execute("select kid,onay,diger,isim,diger2,koku,kelime from osmanlica where isim like '%" + query + "%'")

        else:
            if length == 1:
                cursor.execute("select kid,onay,diger,isim,diger2,koku,kelime from osmanlica where koku like N'" + str(query) 
                            + "%' or diger like N'" + str(query) 
                            + "%' or diger2 like N'" + str(query) 
                            + "%' or kelime like N'" + str(query) + "%'")
            else:
                cursor.execute("select kid,onay,diger,isim,diger2,koku,kelime from osmanlica where diger like N'%" + query
                            + "%' or diger2 like N'%" + query
                            + "%' or koku like N'%" + query
                            + "%' or kelime like N'%" + query + "%'")
        result = cursor.fetchall()

        print(len(result))

        return result
        
    def get(self, request):
        print("get")

        result = None

        user_favorites = FavoritesWord.objects.filter(owner=request.user)

        number_list = [favorite.number for favorite in user_favorites]

        query = request.GET.get('query')
        
        if query:
            print("query: ",query)
            result = self.connect_database(query=query)
            query = None
        
        return render(request, 'lugat.html', {'Sqlserverconn': result, 'user_favorites':number_list})

    def post(self, request):

        favori_id = request.POST.get('favori_id')
        if not FavoritesWord.objects.filter(number=favori_id, owner=request.user).exists():
            word = str(request.POST.get('word'))
            meaning = str(request.POST.get('meaning'))
            FavoritesWord.objects.create(
                number=favori_id,  
                word=''.join(word),      
                meaning=meaning,   
                owner=request.user
            )
        else:
            favorite = FavoritesWord.objects.get(number=favori_id)
            favorite.delete()
        return redirect(request.META.get('HTTP_REFERER', '/'))