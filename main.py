import random
import json
import pickle
import numpy as np
import tensorflow as tf
import nltk
nltk.download('punkt_tab')
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

with open(r"C:\\Users\\saira\\Desktop\\NLP_bot\\intents.json", encoding="utf-8") as file:
    intent = json.load(file)

words = []
classes = []
documents = []
ignore_letters = ['!', '?', '.', ',', "'"]

for intent in intent['intents']:
    for pattern in intent['patterns']:
        # tokenize each word
        wordlist = nltk.word_tokenize(pattern)
        words.extend(wordlist)
        # add documents in the corpus
        documents.append((wordlist, intent['tag']))
        # add to classes if not already there
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_letters]
words = sorted(set(words))
classes = sorted(set(classes))

pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

training = []
output_empty = [0] * len(classes)


for doc in documents:
    bag = []
    pattern_words = doc[0]
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]

    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])

random.shuffle(training)
training = np.array(training, dtype=object)
train_x = np.array(list(training[:, 0]))
train_y = np.array(list(training[:, 1]))

model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(64, activation='relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(len(train_y[0]), activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

sgd = tf.keras.optimizers.SGD(learning_rate=0.01, momentum=0.9, nesterov=True)

model.compile(loss ='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)

model.save('chatbot_model.h5', hist)
print("Training complete. Model saved as 'chatbot_model.h5'.")