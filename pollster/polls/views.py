from django.http.response import Http404, HttpResponseRedirect
from django.urls.base import reverse
from .models import Choice, Question
from django.shortcuts import get_object_or_404, render

# Create your views here.

def index(request):

    latest_questions=Question.objects.order_by('-pub_date')[:5]
    context={
        'latest_questions':latest_questions
    }

    return render(request,'polls/index.html',context)


def details(request,question_id):
    try:
        question=Question.objects.get(pk=question_id)

    except Question.DoesNotExist:
        raise Http404("Question does not exits")

    
    return render(request,'polls/detail.html',{'question':question})

def results(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{
        'question':question
    })


def vote(request,question_id):

    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
            'question':question,
            'error_message':"You didn't select the right choice." 
        })
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))