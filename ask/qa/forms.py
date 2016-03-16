#!/usr/bin/python
# vim: set fileencoding=utf-8
from django import forms
from django.http import HttpResponseRedirect
from qa import models 
from django.contrib.auth.models import User
class AskForm(forms.Form):
	title = forms.CharField(widget=forms.Textarea)
	text  = forms.CharField(widget=forms.Textarea)

	def save(self):
		question = models.Question(**self.cleaned_data)
		question.save()
		return question

class AnswerForm(forms.Form):
    text     = forms.CharField(widget=forms.Textarea)
    question = forms.CharField(widget=forms.HiddenInput())
    def clean(self):
        try:
            question_id = int(self.cleaned_data['question'])
            self.cleaned_data['question'] = question_id
            # if not Question.objects.filter(pk = question_id).count():
            #    raise forms.ValidationError(u'Сообщение не корректно', code=12)
        except ValueError:
            raise forms.ValidationError(u'Сообщение не корректно', code=12)
        return self.cleaned_data
    def save(self):
            answer = models.Answer(question_id = self.cleaned_data['question'], text = self.cleaned_data['text'])
            answer.save()
            return answer



class SignUpForm(forms.Form):
	username = forms.CharField();
	email    = forms.EmailField();
	password = forms.CharField()

	def save(self):
		cd = self.cleaned_data
		user = User.objects.create_user(self.cleaned_data['username'],cd['email'], cd['password']);
		user.save();
		return user;

class LoginForm(forms.Form):
	username = forms.CharField();
	password = forms.CharField()


            
