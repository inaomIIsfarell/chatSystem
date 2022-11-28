from django.shortcuts import HttpResponse, render
from .model.generate import interaction
from .model.args import parse_args
import json

args = parse_args()
global predictor
predictor = interaction(args)


# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request, "index.html")
    else:
        return HttpResponse("Error")


def func(request):
    print(request)
    if request.method == 'GET':
        user_input = request.GET.get('user_input')
        # args = parse_args()
        # predictor = interaction(args)
        print("user_input:", user_input)
        predict = predictor.infer(user_input)
        print("bot:", predict)
        data = {
            'sender': 'transformer',
            'input': user_input,
            'output': predict
        }
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        # args = parse_args()
        # predictor = interaction(args)
        user_input = request.POST.get("user_input")
        print("user_input:", user_input)
        predict = predictor.infer(user_input)
        print("bot:", predict)
        data = {
            'sender': 'transformer',
            'input': user_input,
            'output': predict
        }
        return HttpResponse(json.dumps(data), content_type='application/json')
    # return param
    #  接收post方式传过来的值的方法def func2(request):
    # 查看传输过来的数据类型body = request.body.decode('utf-8')
    # 用json格式转载进来res = json.loads(body)# json.loads() 
    #  json.dumps()区别json.loads()是将字典类型的字符串转换为json格式的字符串。
