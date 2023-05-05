from revChatGPT.V3 import Chatbot


class interaction():
    def __init__(self):
        super(interaction, self).__init__()
        self.model = Chatbot(api_key="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")

    def infer(self, user_input):
        out = self.model.ask(user_input)
        return out
