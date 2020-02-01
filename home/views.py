from django.views.generic import ListView
from .models import Predictor
from django.shortcuts import render

class HomePageView(ListView):
    model= Predictor
    template_name= 'home.html'

    def get(self, request):
        predictions = Predictor.objects.all().order_by('-id')[:5] 
        return render(request, self.template_name, {'predictions':predictions})


class DetailListView(ListView):
    model= Predictor
    template_name= 'detail.html'

    def get(self, request):
        objs = Predictor.objects.all()
        return render(request, self.template_name,{'objs':objs})


    





