from django.db.models.base import Model as Model
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from Hadis_Deryasi.models import FavoritesHadis, FavoritesWord
from Hadis_Deryasi.forms import FavoritesHadisForm, FavoritesWordForm

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class ProfileView(generic.DetailView):

    switch = {'hadis': FavoritesHadis, 'kelime': FavoritesWord}

    def get(self, request):
        favorites_hadis = FavoritesHadis.objects.filter(owner=request.user)
        favorites_kelime = FavoritesWord.objects.filter(owner=request.user)

        form_hadis = FavoritesHadisForm()
        form_kelime = FavoritesWordForm()


        return render(request, 'registration/profile.html', {'favorites_hadis': favorites_hadis, 'favorites_kelime': favorites_kelime,})

    def post(self, request):
        if 'action' in request.POST:
            if request.POST['action'] == 'delete':
                favorite_id = request.POST.get('favorite_id')
                favorite =  self.switch[request.POST.get('favorite_type')].objects.get(pk=favorite_id)
                favorite.delete()
                return redirect('profile')

# zort
        # form = FavoritesForm(request.POST)
        # if form.is_valid():
        #     number = form.cleaned_data['number']
        #     content = form.cleaned_data['content']
        #     FavoritesHadis.objects.create(number=number, content=content, owner=request.user)
        #     return redirect('profile')
        # else:
        #     # Eğer form geçersizse, hata mesajlarını göstermek için kullanabilirsiniz
        #     favorites = FavoritesHadis.objects.filter(owner=request.user)
        #     return render(request, 'registration/profile.html', {'favorites': favorites, 'form': form})

        # Favori düzenleme veya silme işlemleri
        