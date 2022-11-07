from django.shortcuts import render, HttpResponse
from app1.static.model.args import parse_args
from app1.static.model.initialization import init
from app1.static.model.generation import interaction
from paddlenlp.transformers import UnifiedTransformerLMHeadModel, UnifiedTransformerTokenizer

history = []


# Create your views here.
def index(request):
    # 1. 优先去根目录下的templates默认地址寻找
    # 2. 根据app注册顺序，在每个app目录中寻找
    return render(request, "index.html")


def dialogue(request):
    # request是一个对象
    # 封装了用户发送过来的所有请求相关数据

    if request.method == "GET":
        return render(request, "dialogue.html")
    else:
        history.append(request.POST.get("user_input"))
        args = parse_args()
        model, tokenizer = init(args)
        # model = UnifiedTransformerLMHeadModel.from_pretrained(args.model_name_or_path)
        # tokenizer = UnifiedTransformerTokenizer.from_pretrained(args.model_name_or_path)
        # model.eval()
        example = interaction(history)
        history_temp = example.infer(args, model, tokenizer, user_input=request.POST.get("user_input"))
        print("history：", history_temp)
        return render(request, "dialogue.html")
