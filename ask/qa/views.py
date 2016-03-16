from ask import settings
# settings.configure()
from qa.models import Question
from django.http import HttpResponseBadRequest, Http404
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.views.decorators.http import require_GET

# Create your views here.

def test(request, *args, **kwargs):
    return HttpResponse('OK');

def tt(request, *args, **kwargs):
    try:
        page = int(request.GET.get('page', '1'));
    except ValueError:
        raise HttpResponseBadRequest()
    except Question.DoesNotExist:
        raise Http404
    return render(request, 'page.html', { 'page' : page });

@require_GET
def question(request,qid):
    try:
        question = Question.objects.get(pk=qid)
    except Question.DoesNotExist:
        raise Http404
    return render(request, 'question.html', { 
        'question': question, 
        'answers' : question.answer_set.all(),
        'answers_len' : len(question.answer_set.all()) 
    })

@require_GET
def main_pager(request):
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        raise HttpResponseBadRequest()
    except Question.DoesNotExist:
        raise Http404


