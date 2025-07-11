# Streamlit Pkgs
import streamlit as st

# NLP Pkgs
import nltk
from nltk.stem.wordnet import WordNetLemmatizer

from textblob import TextBlob
import re
from nltk.corpus import wordnet as wn

def main():
    # Download Wordnet - lexical database in English
    nltk.download('wordnet')

    st.title("NLP")
    st.subheader("Welcome to our Application")

    text = st.text_area("Enter Your Text")

    if st.button("Analyze"):

        #Text Cleaning
        #Keeping only Text and digits
        text = re.sub(r"[^A-Za-z0-9]", " ", text)
        #Removes Whitespaces
        text = re.sub(r"\'s", " ", text)
        # Removing Links if any
        text = re.sub(r"http\S+", " link ", text)
        # Removes Punctuations and Numbers
        text = re.sub(r"\b\d+(?:\.\d+)?\s+", "", text)
        # Splitting Text
        text = text.split()
    	    
        # Lemmatizer
        lemmatizer = WordNetLemmatizer()
        lemmatized_words =[lemmatizer.lemmatize(word) for word in text]
        text = " ".join(lemmatized_words)
        
        blob = TextBlob(text)
        result = blob.sentiment.polarity

        if result > 0.5:
            custom_emoji = ':blush:'
            st.success('Happy : {}'.format(custom_emoji))
        elif result > 0.0:
            custom_emoji = ':worried:'
            st.warning('Worried : {}'.format(custom_emoji))
        elif result < 0.0:
            custom_emoji = ':disappointed:'
            st.warning('Disappointed : {}'.format(custom_emoji))
        else:
            custom_emoji = ':confused:'
            st.info('Confused : {}'.format(custom_emoji))

        st.success("Polarity Score is: {}".format(result))

if __name__ == '__main__':
    main()
