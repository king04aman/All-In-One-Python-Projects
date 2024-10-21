import pandas as pd
import numpy as np
import json
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
import os

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('wordnet')

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Load datasets
try:
    print("Files in current directory:", os.listdir())
    csv_files = [f for f in os.listdir() if f.endswith('.csv') and 'Combined' in f and 'Data' in f]
    if csv_files:
        df = pd.read_csv(csv_files[0])
        print(f"Loaded file: {csv_files[0]}")
        print("DataFrame columns:", df.columns.tolist())
        print("DataFrame shape:", df.shape)
        print(df.head())
    else:
        raise FileNotFoundError("No matching CSV file found")
except FileNotFoundError as e:
    print(f"Error: {str(e)}")
    print("Ensure 'Combined_Data.csv' is in the same directory.")
    print("Current working directory:", os.getcwd())
    exit(1)

# Load intents.json
try:
    with open('intents.json', 'r') as f:
        intents = json.load(f)
except FileNotFoundError as e:
    print(f"Error: {str(e)}. Ensure 'intents.json' is available.")
    exit(1)

# Preprocess text data
def preprocess_text(text):
    tokens = nltk.word_tokenize(str(text).lower())
    return ' '.join([lemmatizer.lemmatize(token) for token in tokens])

# Determine the correct column name for text data
text_column = 'statement' if 'statement' in df.columns else df.columns[0]

df['processed_text'] = df[text_column].apply(preprocess_text)

# Create TF-IDF vectorizer
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['processed_text'])

# Prepare data for model training
X, y = [], []

for intent in intents['intents']:
    for pattern in intent['patterns']:
        X.append(preprocess_text(pattern))
        y.append(intent['tag'])

X = vectorizer.transform(X).toarray()
y = pd.get_dummies(y).values

# Ensure X and y have the same shape
assert X.shape[0] == y.shape[0], f"Shape mismatch: X={X.shape}, y={y.shape}"

# Build the model
model = Sequential([
    Dense(128, input_shape=(X.shape[1],), activation='relu'),
    Dropout(0.5),
    Dense(64, activation='relu'),
    Dropout(0.5),
    Dense(y.shape[1], activation='softmax')
])

model.compile(optimizer=Adam(learning_rate=0.01), loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model with error handling
try:
    model.fit(X, y, epochs=200, batch_size=32, verbose=1)
except Exception as e:
    print(f"Error during model training: {str(e)}")
    print(f"X shape: {X.shape}, y shape: {y.shape}")
    raise

# Chatbot function
def chatbot_response(user_input):
    processed_input = preprocess_text(user_input)
    input_vector = vectorizer.transform([processed_input]).toarray()

    # Find similar responses from the dataset
    similarities = cosine_similarity(input_vector, tfidf_matrix)
    most_similar_idx = similarities.argmax()
    response = df.iloc[most_similar_idx][text_column]

    # Classify intent
    intent_probs = model.predict(input_vector)[0]
    intent_idx = intent_probs.argmax()
    intent_tag = list(pd.get_dummies([i['tag'] for i in intents['intents']]).columns)[intent_idx]

    # Get response from intents
    for intent in intents['intents']:
        if intent['tag'] == intent_tag:
            intent_response = np.random.choice(intent['responses'])
            break

    return f"Dataset Response: {response}\n\nIntent Response: {intent_response}"

# Main chat loop
print("Mental Health Chatbot: Hello! I'm here to provide support and resources for mental health. How can I help you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() in ['quit', 'exit', 'bye']:
        print("Mental Health Chatbot: Take care! Remember, it's okay to seek help when you need it.")
        break
    response = chatbot_response(user_input)
    print("Mental Health Chatbot:", response)

