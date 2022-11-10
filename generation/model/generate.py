from generation.static.plugins.utils import select_response
from paddlenlp.transformers import UnifiedTransformerTokenizer, UnifiedTransformerLMHeadModel


class interaction():
    def __init__(self, args):
        super(interaction, self).__init__()
        self.args = args
        self.model = UnifiedTransformerLMHeadModel.from_pretrained(self.args.model_name_or_path)
        self.tokenizer = UnifiedTransformerTokenizer.from_pretrained(self.args.model_name_or_path)
        self.model.eval()

    def infer(self, user_input):
        encoded_input = self.tokenizer.dialogue_encode(
            user_input,
            add_start_token_as_response=True,
            return_tensors=True,
            is_split_into_words=False
        )
        ids, scores = self.model.generate(
            input_ids=encoded_input['input_ids'],
            token_type_ids=encoded_input['token_type_ids'],
            position_ids=encoded_input['position_ids'],
            attention_mask=encoded_input['attention_mask'],
            decode_strategy=self.args.decode_strategy,
            top_k=self.args.top_k,
            num_return_sequences=self.args.num_return_sequence
        )
        predict = select_response(
            ids,
            scores,
            self.tokenizer,
            self.args.max_dec_len,
            self.args.num_return_sequence,
            keep_space=False
        )[0]
        return predict
