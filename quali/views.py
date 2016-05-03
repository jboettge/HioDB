from django.shortcuts import render

from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render
from .models import quali
# Create your views here.
def index(request):
    latest_question_list = quali.objects.order_by('-date')[:5]
    template = loader.get_template('quali/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, quali_id):
    try:
        quali = quali.objects.get(pk=quali_id)
    except quali.DoesNotExist:
        raise Http404("quali does not exist")
    return render(request, 'quali/detail.html', {'quali': quali})


def results(request, quali_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % quali_id)

def vote(request, quali_id):
    return HttpResponse("You're voting on question %s." % quali_id)