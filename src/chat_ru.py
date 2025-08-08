from main_chat import ChatBot
import pandas as pd
from accessify import private


class RuChatBot(ChatBot):
    def __init__(self):
        super().__init__()
        self.build()

    @private
    def build(self):
        pass

    def get(self):
        pass
