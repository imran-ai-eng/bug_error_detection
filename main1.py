import streamlit as st
import pickle
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def clean_code(text):
    text=re.sub(r'[^a-zA-Z0-9_\s]',' ' ,text) #remove special characters
    tokens=word_tokenize(text.lower()) #Tokenization and lowercasing
    tokens=[word for word in tokens if word not in stopwords.words('english')]
    return ' '.join(tokens) 
st.title("Bug Prediction and Prevention System")
st.write("Enter a Python code to check if it contain a bug.")
user_input=st.text_area("Enter Code Snippet")
button=st.button("Predict!")
if button:
    vectorizer=pickle.load(open('x_tfitf.pkl','rb'))
    model=pickle.load(open('rf.pkl','rb'))
    
    cleaned_code=clean_code(user_input)
    input_tfidf=vectorizer.transform([cleaned_code])
    predict=model.predict(input_tfidf)[0]
    
    if predict:
        st.error("Bug Detected")
    else:
        st.success(" No Bug Detected")