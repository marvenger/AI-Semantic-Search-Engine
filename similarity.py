#!/usr/bin/env python
# coding: utf-8




import numpy as np
import pinecone

def cosine_similarity(vectors1, vectors2):
    """
    Computes the cosine similarity between two vectors.
    
    Args:
    vectors1 (numpy array): The first vector.
    vectors2 (numpy array): The second vector.
    
    Returns:
    The cosine similarity between the two vectors.
    """
    dot_product = np.dot(vectors1, vectors2)
    norm1 = np.linalg.norm(vectors1)
    norm2 = np.linalg.norm(vectors2)
    return dot_product / (norm1 * norm2)

def search(query, index_name, top_k=10):
    """
    Searches the vector database for documents similar to the user's query.
    
    Args:
    query (numpy array): The user's query in vector form.
    index_name (str): The name of the Pinecone index to search.
    top_k (int): The number of top search results to return.
    
    Returns:
    A list of the top_k most similar document IDs to the user's query.
    """
    # Connect to the Pinecone vector database
    pinecone.init(api_key="YOUR_API_KEY")
    index = pinecone.Index(index_name)

    # Search the index for similar documents
    result_ids, _ = index.query(queries=query, top_k=top_k)

    # Return the IDs of the most similar documents
    return result_ids

