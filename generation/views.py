from django.shortcuts import render, HttpResponse
from .model.generate import interaction
from .model.args import parse_args
import json


# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request, "index.html")
    else:
        return HttpResponse("Error")


def dialogue(request):
    if request.method == 'GET':
        return render(request, "index.html")
    else:
        args = parse_args()
        predictor = interaction(args)
        user_input = request.POST.get("user_input")
        print("user_input:", user_input)
        predict = predictor.infer(user_input)
        print("bot:", predict)
        data = {
            'sender' : 'transformer',
            'input' : user_input,
            'output' : predict
        }
        return HttpResponse(json.dumps(data), content_type='application/json')

    # args = parse_args()
    # predictor = interaction(args)
    # user_input = request.POST.get("user_input")
    # bot_response = predictor.infer(user_input)
    # return HttpResponse(bot_response)
