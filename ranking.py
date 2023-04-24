#!/usr/bin/env python
# coding: utf-8




import numpy as np

def rank_documents(query, documents):
    """
    Ranks the documents based on their relevance to the query.

    Args:
    - query: str, the user's search query.
    - documents: dict, a dictionary where each key is a document ID and each value is a dictionary containing the document's
                 text, score and other metadata.

    Returns:
    - ranked_documents: list of tuples, each tuple contains a document ID and its relevance score to the query.
    """

    # Calculate the cosine similarity between the query and each document
    similarities = {}
    query_vector = query.get_vector()
    for doc_id, doc in documents.items():
        doc_vector = doc.get_vector()
        similarity = np.dot(query_vector, doc_vector) / (np.linalg.norm(query_vector) * np.linalg.norm(doc_vector))
        similarities[doc_id] = similarity

    # Sort the documents in descending order of their similarity to the query
    ranked_documents = sorted(similarities.items(), key=lambda x: x[1], reverse=True)

    return ranked_documents

