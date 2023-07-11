from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import Question, Choice
from django.utils import timezone
from django.db import connection
from datetime import datetime
from dateutil.tz import tzutc
""" def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
 """
@csrf_exempt
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
 
@csrf_exempt
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

@csrf_exempt
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

#2023-07-04 17:40:17.968230+00:00
@csrf_exempt
def create_new(request):
    if request.method == "POST":
        new_q = request.body.decode("utf-8").replace("create_new=","")
        print(new_q)
        count = 0
        for p in Question.objects.all():
            count += 1
        newid = count+1
        #q = Question(question_text=new_q, pub_date=timezone.now())
        #q.save()
        #q.id
        #q.choice_set.create(choice_text='Not much', votes=0)
        #q.choice_set.create(choice_text="the other answer", votes=0)
        # sarakkeet ['id', 'question_text', 'pub_date']
        aika = str(datetime.now(tz=tzutc()))
        insert = f"INSERT INTO polls_question (id, question_text, pub_date) VALUES ( {str(newid)}, {str(new_q)}, {aika} )"
        x = Question.objects.raw( insert)
            #Question.objects.raw( )
        # 'SELECT * FROM polls_question WHERE question_text="What's up?"'
        pid = 0
        #for p in Question.objects.raw('SELECT * FROM polls_question'):
        #for p in Question.objects.raw('SELECT * FROM polls_question WHERE question_text="asd"'):
        #    print(p.id)
        #    i += 1
        #    pid = p.id
        haettu = Question.objects.get(pk=newid)
        haettu.save()
        #print("haettu:", haettu)
        #haettu.delete()
        #for p in Question.objects.all():
        #    print(p)
    return render(request, 'polls/create.html')

@csrf_exempt
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        print("selected choice",selected_choice)
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
