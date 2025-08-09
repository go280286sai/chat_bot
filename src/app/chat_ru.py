from main_chat import ChatBot
import pandas as pd
from accessify import private
import pymorphy3
from helps.help_words import get_words


class RuChatBot(ChatBot):
    def __init__(self):
        super().__init__()
        self.stop_words = get_words("russian")
        self.build()

    def build(self):
        pass

    def get(self, message: str):
        morph = pymorphy3.MorphAnalyzer(lang='ru')
        result = [morph.parse(item)[0].normal_form for item in message.lower().split() if item not in self.stop_words]
        return result


obj = RuChatBot()
obj.build()
print(obj.get("Сегодня стояла прекрасная погода и птички пели громко"))
