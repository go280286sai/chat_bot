"""
Chat Ukrainian Bot
"""
# pylint: disable=invalid-name
import re
import random
import logging
import joblib
import pandas as pd
import pymorphy3

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from helps.help_words import get_words


class UkChatBot:
    """
    Chat Ukrainian Bot
    """

    def __init__(self, data: list):
        self.stop_words = get_words("ukraine")
        self.morph = pymorphy3.MorphAnalyzer(lang='uk')
        self.model_path = 'files/model_uk.pkl'
        self.vector_path = 'files/vector_uk.pkl'
        self.model = None
        self.vector = None

        questions_df = pd.DataFrame(data)
        questions = questions_df[
            questions_df['language_id'] == 2
            ].reset_index(drop=True)
        questions.drop(columns=[
            'language_id',
            'id',
            'language',
            'category'
        ], inplace=True, errors='ignore')
        questions['name'] = questions['name'].apply(self.clean_data)

        self.build(questions)

    def build(self, data: pd.DataFrame):
        """
        Creates model and vectorizer
        """
        self.vector = TfidfVectorizer()
        if self.vector is not None:
            X = self.vector.fit_transform(data['name'])
        else:
            raise ValueError("Vectorizer is not initialized")
        y = data['category_id']
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2,
            random_state=0, shuffle=True
        )

        self.model = RandomForestClassifier(
            max_depth=7,
            random_state=0,
            n_estimators=150,
            n_jobs=-1
        )
        self.model.fit(X_train, y_train)

        predictions = self.model.predict(X_test)
        acc = accuracy_score(y_test, predictions)
        logging.info("Ukrainian model accuracy: %.4f", acc)

        joblib.dump(self.model, self.model_path)
        joblib.dump(self.vector, self.vector_path)

    def clean_data(self, message: str) -> str:
        """
        Cleans data
        """
        message = re.sub(r'[^\w\s]', '', message.lower())
        tokens = message.split()
        normalized = [
            self.morph.parse(word)[0].normal_form
            for word in tokens if word not in self.stop_words
        ]
        return ' '.join(normalized)

    def get_predict(self, message: str) -> int | None:
        """
        Predicts category
        """
        if self.model is None or self.vector is None:
            self.model = joblib.load(self.model_path)
            self.vector = joblib.load(self.vector_path)

        cleaned = self.clean_data(message)
        if self.vector is not None:
            transformed = self.vector.transform([cleaned])
        else:
            raise ValueError("Vectorizer is not initialized")
        prediction = self.model.predict(transformed)
        return prediction.tolist()[0] if prediction else None

    def get_answer(self, data: list, predict: int) -> str | None:
        """
        Gets answer
        """
        answers_df = pd.DataFrame(data)
        answers = answers_df[
            (answers_df['language_id'] == 2) &
            (answers_df['category_id'] == predict)
            ].reset_index(drop=True)

        if answers.empty:
            logging.warning("No answers found for category_id=%d", predict)
            return None

        return random.choice(answers['name'].tolist())
