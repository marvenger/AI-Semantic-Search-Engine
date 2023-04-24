#!/usr/bin/env python
# coding: utf-8



import spacy
import en_core_web_sm
from typing import List

# Load the spacy English language model
nlp = en_core_web_sm.load()

def extract_entities(text: str) -> List[str]:
    """
    Extract named entities (people, places, organizations) from text.
    Args:
        text (str): Input text
    Returns:
        List[str]: List of named entities extracted from the text
    """
    # Parse the input text using the spacy model
    doc = nlp(text)
    
    # Extract named entities from the parsed text
    entities = [ent.text for ent in doc.ents if ent.label_ in ["PERSON", "ORG", "GPE"]]
    
    # Return the list of named entities
    return entities

