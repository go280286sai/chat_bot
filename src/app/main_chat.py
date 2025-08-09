from abc import ABC, abstractmethod



class ChatBot(ABC):
    @abstractmethod
    def build(self):
        pass

    @abstractmethod
    def get(self, message: str):
        pass

