from django.http import HttpResponseBadRequest, Http404
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.views.decorators.http import require_GET
from qa.models import Question,Answer
from django.core.paginator import Paginator

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
def main_pager(request):
    limit = 10
    try:
        page = int(request.GET.get('page', '1'))
        questions = Question.objects.order_by('-added_at')
        paginator = Paginator(questions, limit)
        paginator.baseurl = "/?page="
        page = paginator.page(page)
    except ValueError:
        raise HttpResponseBadRequest()
    except Question.DoesNotExist:
        raise Http404
    return render(
        request,
        'main.html',
        {
            'questions' : page.object_list,
            'page' : page,
            'paginator':paginator,
        }
    );
@require_GET
def popular_pager(request):
    limit = 10
    try:
        page = int(request.GET.get('page', '1'))
        questions = Question.objects.order_by('-rating')
        paginator = Paginator(questions, limit)
        paginator.baseurl = "/popular/?page="
        page = paginator.page(page)
    except ValueError:
        raise HttpResponseBadRequest()
    except Question.DoesNotExist:
        raise Http404
    return render(
        request,
        'main.html',
        {
            'questions' : page.object_list,
            'page' : page,
            'paginator':paginator,
        }
    );


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
