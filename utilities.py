#!/usr/bin/env python
# coding: utf-8



import re
import json

def clean_text(text):
    """
    This function receives a string of text and returns a clean version of it,
    removing any special characters, punctuation, and extra whitespaces.
    """
    text = re.sub(r'[^\w\s]', '', text) # remove special characters and punctuation
    text = re.sub(r'\s+', ' ', text) # replace extra whitespaces with a single space
    text = text.lower().strip() # convert to lowercase and remove leading/trailing whitespaces
    return text

def load_stopwords(lang='en'):
    """
    This function loads the stopwords for a given language from a text file and
    returns them as a list of strings.
    """
    with open(f'data/stopwords_{lang}.txt', 'r', encoding='utf-8') as f:
        stopwords = [word.strip() for word in f]
    return stopwords

def load_stopwords(lang='fr'):
    """
    This function loads the stopwords for a given language from a text file and
    returns them as a list of strings.
    """
    with open(f'data/stopwords_{lang}.txt', 'r', encoding='utf-8') as f:
        stopwords = [word.strip() for word in f]
    return stopwords

def load_embeddings(lang='en'):
    """
    This function loads the pre-trained word embeddings for a given language from a binary file
    and returns them as a dictionary where the keys are the words and the values are the vectors.
    """
    with open(f'models/{lang}_embedding.bin', 'rb') as f:
        embeddings = json.load(f)
    return embeddings

def load_embeddings(lang='fr'):
    """
    This function loads the pre-trained word embeddings for a given language from a binary file
    and returns them as a dictionary where the keys are the words and the values are the vectors.
    """
    with open(f'models/{lang}_embedding.bin', 'rb') as f:
        embeddings = json.load(f)
    return embeddings

def load_synonyms(lang='en'):
    """
    This function loads the synonym mappings for a given language from a JSON file
    and returns them as a dictionary where the keys are the original words and the values
    are the lists of synonyms.
    """
    with open(f'models/synonyms_{lang}.json', 'r', encoding='utf-8') as f:
        synonyms = json.load(f)
    return synonyms

def load_synonyms(lang='fr'):
    """
    This function loads the synonym mappings for a given language from a JSON file
    and returns them as a dictionary where the keys are the original words and the values
    are the lists of synonyms.
    """
    with open(f'models/synonyms_{lang}.json', 'r', encoding='utf-8') as f:
        synonyms = json.load(f)
    return synonyms

