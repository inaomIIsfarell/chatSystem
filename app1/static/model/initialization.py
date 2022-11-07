from paddlenlp.transformers import UnifiedTransformerLMHeadModel, UnifiedTransformerTokenizer
import paddle

def init(args):
    paddle.set_device(args.device)
    model = UnifiedTransformerLMHeadModel.from_pretrained(args.model_name_or_path)
    tokenizer = UnifiedTransformerTokenizer.from_pretrained(args.model_name_or_path)
    model.eval()
    return model, tokenizer