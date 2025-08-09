import pandas as pd
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


# Скачать ресурсы NLTK
nltk.download('punkt')
nltk.download('wordnet')
stop_words = set(ENGLISH_STOP_WORDS)

lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    tokens = word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return ' '.join(tokens)

data = pd.read_csv("words.csv", sep=";").reset_index(drop=True)
data["cleaner"] = data['body'].apply(preprocess_text)

y = data["target"].values
tfid = TfidfVectorizer(max_features=5000)
X = tfid.fit_transform(data["cleaner"].values)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=True, random_state=42)
model = RandomForestRegressor(random_state=0, n_estimators=170, n_jobs=-1, max_depth=11)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(mean_squared_error(y_test, y_pred))

text = "how to pay this product"
new_text = tfid.transform([text])
print(round(model.predict(new_text)[0]))
