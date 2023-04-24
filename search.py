#!/usr/bin/env python
# coding: utf-8




import pinecone
import numpy as np
from src.similarity import cosine_similarity
from src.ranking import rank_documents

# Define the search function that takes in the user's query and returns the most relevant documents
def search(query, index_name, language, top_k=10):
    
    # Connect to the Pinecone vector database and get the index
    pinecone.init(api_key='YOUR_API_KEY')
    index = pinecone.Index(index_name)
    
    # Get the vector representation of the query using the specified language's embedding model
    if language == 'en':
        # Load the English embedding model from the models folder
        from models.english_embedding import embed
        query_vector = embed(query)
    elif language == 'fr':
        # Load the French embedding model from the models folder
        from models.french_embedding import embed
        query_vector = embed(query)
    else:
        # If the language is not supported, return an error message
        return 'Language not supported'
    
    # Use the Pinecone index to search for the most similar documents to the query vector
    response = index.query(queries=[query_vector], top_k=top_k)
    
    # Get the ids and vectors of the top-k most similar documents
    ids = response.ids
    vectors = np.array(response.vectors)
    
    # Calculate the cosine similarity between the query vector and the top-k document vectors
    similarities = cosine_similarity(query_vector, vectors)
    
    # Rank the documents based on their similarity to the query
    ranked_ids = rank_documents(ids, similarities)
    
    # Return the ids of the top-k most relevant documents
    return ranked_ids

