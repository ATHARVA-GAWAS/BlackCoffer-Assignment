from django.shortcuts import *
from django.http import *
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Data
from plotly.offline import plot
import plotly.express as px

from django.views.generic import TemplateView
# Create your views here.

def index(request):
    return render(request,'test.html')
    
def chart(request):
    co2=Data.objects.all()
    fig=px.line(
        x=[c.intensity for c in co2],
        y=[c.relevance for c in co2]
        
        )
    chart=fig.to_html()
    context={'chart':chart}
    return render(request,'test.html',context)

@csrf_exempt

#def barchart(request):
#    co2=Data.objects.all()
#    x=[c.sector for c in co2],
#    y=[c.likelihood for c in co2]
#    context={}
#    return render(request,'test.html',context)

def scatterchart(request):
    co2=Data.objects.all()
    fig=px.scatter(
        x=[c.likelihood for c in co2],
        y=[c.relevance for c in co2]
        )
    scatterchart=plot(fig,output_type="div")
    context={'scatterchart':scatterchart}
    return render(request,'test.html',context)

def save_json(request):
    if request.method=='POST':
        payload=json.loads(request.body)
        end_year=payload.get('end_year')
        intensity=payload.get('intensity')
        sector=payload.get('sector')
        topic=payload.get('topic')
        insight=payload.get('insight')
        url=payload.get('url')
        region=payload.get('region')
        start_year=payload.get('start_year')
        impact=payload.get('impact')
        added=payload.get('added')
        published=payload.get('published')
        country=payload.get('country')
        relevance=payload.get('relevance')
        pestle=payload.get('pestle')
        source=payload.getd('source')
        title=payload.get('title')
        likelihood=payload.get('likelihood')
    return HttpResponse('Json Data has been saved')    

class ClubChartView(TemplateView):
    template_name='test.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["qs"]=Data.objects.all()
        return context