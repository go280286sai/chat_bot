"""
Main chat bot
"""
# pylint: disable=too-few-public-methods
import logging
from src.app.chat_en import EnChatBot
from src.app.chat_ru import RuChatBot
from src.app.chat_uk import UkChatBot
from src.models.answers_database import AnswersDatabase
from src.models.questions_database import QuestionsDatabase


class MainChat:
    """
    Main chat bot
    """

    def __init__(self):
        try:
            answers_database = AnswersDatabase()
            questions_database = QuestionsDatabase()
            self.answers_data = answers_database.get_all()
            questions_data = questions_database.get_all()
            self.ru_chat_bot = RuChatBot(questions_data)
            self.uk_chat_bot = UkChatBot(questions_data)
            self.en_chat_bot = EnChatBot(questions_data)
        except ValueError as e:
            logging.error(e)

    def get(self, message: str, lang: str) -> str | None:
        """
        Main chat bot get
        :param message:
        :param lang:
        :return:
        """
        try:
            chat_bots = {
                'en': self.en_chat_bot,
                'uk': self.uk_chat_bot,
                'ru': self.ru_chat_bot
            }

            bot = chat_bots.get(lang)
            if not bot:
                raise ValueError(f"Unsupported language: {lang}")

            question = bot.get_predict(message=message)
            if not question:
                raise ValueError("Question fail")

            answer = bot.get_answer(data=self.answers_data, predict=question)
            if not answer:
                raise ValueError("Answer fail")

            return answer
        except ValueError as e:
            logging.error(e)
            return None
