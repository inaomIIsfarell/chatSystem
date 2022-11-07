from termcolor import colored, cprint
from ..plugins import utils


class interaction():
    def __init__(self, history):
        super().__init__()
        self.history = history

    def infer(self, args, model, tokenizer, user_input):
        start_info = "Enter [NEXT] to start a new conversation, Enter [EXIT] to quit the conversation"
        cprint(start_info, "yellow", attrs=["bold"])
        if user_input == "[EXIT]":
            return
        elif user_input == "[NEXT]":
            self.history = []
            cprint(start_info, "yellow", attrs=["bold"])
        else:
            # self.history.append(user_input)
            inputs = tokenizer.dialogue_encode(
                self.history,
                add_start_token_as_response=True,
                return_tensors=True,
                is_split_into_words=False
            )
            ids, scores = model.generate(
                inputs_ids=inputs['input_ids'],
                token_type_ids=inputs['token_type_ids'],
                position_ids=inputs['position_ids'],
                attention_mask=inputs['attention_mask'],
                max_length=args.max_dec_len,
                min_length=args.min_dec_len,
                decode_strategy=args.decode_strategy,
                top_k=args.top_k,
                num_return_sequences=args.num_return_sequence
            )
            bot_response = utils.select_response(
                ids=ids,
                scores=scores,
                tokenizer=tokenizer,
                max_dec_len=args.max_dec_len,
                num_return_sequences=args.num_return_sequence,
                keep_space=False
            )[0]
            self.history.append(bot_response)
            print(colored("[Bot]:", "blue", attrs=["bold"]), colored(bot_response, attrs=["bold"]))
            return self.history
