from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from polls.models import Question, Choice


def index(request):
    questions = Question.objects.all()
    context = {
        'questions': questions,
    }
    return render(request, 'polls/index.html', context)


def detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    context = {
        'question': question,
    }
    return render(request, 'polls/detail.html', context)


def vote(request, pk):
    if request.method == 'POST':
        question = Question.objects.get(pk=pk)
        choice_pk = request.POST['vote']
        choice = Choice.objects.get(pk=choice_pk)
        choice.votes += 1
        choice.save()
        return redirect('detail', pk=question.pk)
    else:
        return HttpResponse('Permission denied')
