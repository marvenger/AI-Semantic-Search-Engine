#!/usr/bin/env python
# coding: utf-8




from flask import Flask, render_template, request
import os
import json
from src import vectorization, similarity, ranking, language_detection, third_party_integration

# Initialize Flask app
app = Flask(__name__)

# Load vectorizer model
vectorizer_en = vectorization.load_vectorizer('models/english_embedding.bin')
vectorizer_fr = vectorization.load_vectorizer('models/french_embedding.bin')

# Load stop words for each language
stop_words_en = vectorization.load_stopwords('data/stopwords_en.txt')
stop_words_fr = vectorization.load_stopwords('data/stopwords_fr.txt')

# Load synonyms
with open('models/synonyms_en.json') as f:
    synonyms_en = json.load(f)

# Load documents for each language
documents_en = vectorization.load_documents('data/documents_en.csv')
documents_fr = vectorization.load_documents('data/documents_fr.csv')

# Initialize vector database
database = third_party_integration.initialize_database()

# Home page
@app.route('/')
def home():
    return render_template('search.html')

# Search page
@app.route('/search', methods=['POST'])
def search():
    # Get user query from form
    user_query = request.form['query']
    # Detect user query language
    query_language = language_detection.detect_language(user_query)
    # Vectorize user query based on language
    if query_language == 'en':
        user_query_vector = vectorization.vectorize_text(user_query, vectorizer_en, stop_words_en)
    elif query_language == 'fr':
        user_query_vector = vectorization.vectorize_text(user_query, vectorizer_fr, stop_words_fr)
    else:
        return render_template('search.html', error='Unsupported language')
    # Search vector database for similar documents
    similar_documents_indices = similarity.search_database(database, user_query_vector)
    # Rank similar documents based on relevance to user query
    ranked_documents_indices = ranking.rank_documents(user_query_vector, similar_documents_indices, 
                                                       documents_en if query_language == 'en' else documents_fr)
    # Extract entities from ranked documents
    ranked_documents_with_entities = third_party_integration.extract_entities(ranked_documents_indices, 
                                                                                documents_en if query_language == 'en' else documents_fr)
    # Render search results page
    return render_template('search.html', query=user_query, ranked_documents=ranked_documents_with_entities, 
                           query_language=query_language, synonyms=synonyms_en)

# Run app
if __name__ == '__main__':
    app.run(debug=True)

