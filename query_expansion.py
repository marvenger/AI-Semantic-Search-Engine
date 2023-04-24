#!/usr/bin/env python
# coding: utf-8



import json

def expand_query(query, synonyms_file):
    """
    Expands the user's query to include synonyms of the words in the query.

    Parameters:
    query (str): User's search query
    synonyms_file (str): Path to the JSON file containing synonyms for the words in the query

    Returns:
    expanded_query (str): The original query with additional synonyms included
    """

    # Load the JSON file containing synonyms
    with open(synonyms_file, 'r') as f:
        synonyms = json.load(f)

    # Split the query into individual words
    words = query.split()

    # Initialize a list to hold the expanded query
    expanded_query = []

    # Iterate through each word in the query
    for word in words:

        # If the word has synonyms, add them to the expanded query
        if word in synonyms:
            expanded_query.extend(synonyms[word])

        # Add the original word to the expanded query
        expanded_query.append(word)

    # Combine the expanded query into a single string
    expanded_query = ' '.join(expanded_query)

    return expanded_query

