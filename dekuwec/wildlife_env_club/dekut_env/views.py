from django.template import loader
from django.http import HttpResponse
from .models import Official

def dekut_env(request):
    officials = Official.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'officials' : officials,
    }
    return HttpResponse(template.render(context, request))
