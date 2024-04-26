# Import Library
import numpy as np
import random
import pickle
from Intent import Intents
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from keras.models import load_model

# Data Loading
words = pickle.load(open('words.pickle','rb'))
classes = pickle.load(open('classes.pickle', 'rb'))
model = load_model('chatbot_model.h5')

# Text Preprocessing for Input
def preprocess_sentence(sentence):
    # Tokenization
    tokenized_sentence = word_tokenize(sentence)
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_sentence = [lemmatizer.lemmatize(word.lower()) for word in tokenized_sentence]
    return lemmatized_sentence

# Text Vectorization for Input
def bow(sentence, words, show_details=True):
    # preprocess the sentence
    sentence_words = preprocess_sentence(sentence)
    # Generate bag of words
    bag = [0]*len(words)
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

# Model Prediction
def predict_class(sentence, model):
    # Generate BOW
    p = bow(sentence, words, show_details=False)
    
    # Model prediction
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]

    # Sort result by error threshold
    results.sort(key=lambda x: x[1], reverse=True)

    # Organize result in format (intent, probability)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

# Handle Output
def getResponse(ints, intents):
    tag = ints[0]['intent']
    for IntentInfo in Intents:
        if(IntentInfo['intent']== tag):
            result = random.choice(IntentInfo['responses'])
            break
    return result

# AI Chatbot Response
def chatbot_response(msg):
    pred_ints = predict_class(msg, model)
    res = getResponse(pred_ints, Intents)
    return res

# Testing & Debugging
def Testing():
    sentence = "I wanna take a data engineering courses"
    output = predict_class(sentence, model)
    print(output)

    sentence = "I wanna be a data scientist"
    res = chatbot_response(sentence)
    print(res)
