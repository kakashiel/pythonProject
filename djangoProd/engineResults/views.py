import requests
import json 
from datetime import datetime, timezone
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import QuestionForm
from django.conf import settings

#post request to docQA
def get_answers(question):
    headers = {'Content-type': 'application/json','Accept': 'text/plain'}
    url = settings.URL 
    data = {'question': question}
    r = requests.post(url, json={"question": question}, headers=headers)
    answers = r.json()
    answer_list = answers['liste']
    print(answer_list)
    return answer_list

#Calcul le temps de creation d'un compte
def user_expire(request):
    date =  datetime.now(timezone.utc) - request.user.date_joined
    days, seconds = date.days, date.seconds
    return days * 24 + seconds // 3600 >= settings.TIMESESSIONEXPIRE

@login_required(login_url='/users/login/')
def get_question(request):
    if user_expire(request):
        return render(request, 'account_out_of_date.html', {})
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data['your_question']
            reponse = get_answers(question)
            print(reponse)
            return render(request, 'question.html', {'form': form, 'result': reponse})
    else:
        form = QuestionForm()
    return render(request, 'question.html', {'form': form})
