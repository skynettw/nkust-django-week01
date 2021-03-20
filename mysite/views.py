from django.shortcuts import render
from django.http import HttpResponse
import random, datetime

def index(request):
	return render(request, "index.html", locals())
	
def lotto(request):
	numbers = [n for n in range(1, 43)]
	random.shuffle(numbers)
	lotto = numbers[:6]
	special = numbers[6]
	return render(request, "lotto.html", locals())

def date(request):
	now = datetime.datetime.now()
	return HttpResponse("現在時刻：{}".format(now))
