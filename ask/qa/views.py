#!/usr/bin/python
# vim: ts=4 ts=4 sts=4 et
from django.http import HttpResponseBadRequest, Http404
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.views.decorators.http import require_GET
from qa.models import Question,Answer
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from qa.forms import AskForm,AnswerForm, LoginForm, SignUpForm

# Create your views here.

def my_login(request):
    form = LoginForm()
    ok = True
    user = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        user = authenticate(username=request.POST.get('username',''), password=request.POST.get('password',''))
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/')
        ok = False
    return render(request, 'my_login.html', { 'form':form, 'user': user, 'ok': ok })

def my_signup(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user2 = authenticate(username=request.POST.get('username',''), password=request.POST.get('password',''))
            login(request,user2)
            return HttpResponseRedirect('/')
    return render(request, "my_signup.html", { 'form' : form });


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

def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            form._user = request.user
            question = form.save()
            return HttpResponseRedirect(question.get_url())

        return HttpResponse(request.method);
    elif request.method == 'GET':
        form = AskForm()

    return render(request,"ask_form.html", { "form" : form, "user": request.user })


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
            'user': request.user,
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
        'popular.html',
        {
            'questions' : page.object_list,
            'page' : page,
            'paginator':paginator,
        }
    );


def answer(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form._user = request.user
            answer = form.save()
            return HttpResponseRedirect(answer.question.get_url())
    return question(request,form.cleaned_data["question_id"],form = form)

def question(request,qid, form=None):
    try:
        question = Question.objects.get(pk=qid)
    except Question.DoesNotExist:
        raise Http404
            
    if not form:
        form = AnswerForm( { "question" : qid } )

    return render(request, 'question.html', { 
        'question': question, 
        'answers' : question.answer_set.all(),
        'answers_len' : len(question.answer_set.all()),
        'form' : form,
        "user" : request.user,
    })
