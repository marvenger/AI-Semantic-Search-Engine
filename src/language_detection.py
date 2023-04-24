#!/usr/bin/env python
# coding: utf-8



from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException

def detect_language(text):
    """
    Function to detect the language of a given text using the langdetect package
    
    Args:
        text (str): The text to detect the language for
    
    Returns:
        lang (str): The detected language
    """
    try:
        lang = detect(text)
        return lang
    except LangDetectException:
        # If langdetect is not able to detect the language, return None
        return None

