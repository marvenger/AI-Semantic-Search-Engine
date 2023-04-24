# AI-Semantic-Search-Engine
This is a search engine project that provides a user interface for searching documents in English and French. The project was developed in Python using various libraries and technologies.


## Search Engine Project
This is a search engine project that provides a user interface for searching documents in English and French. The project was developed in Python using various libraries and technologies.

## Project Structure
The project is structured as follows:


├── data
│   ├── documents_en.csv
│   ├── documents_fr.csv
│   ├── stopwords_en.txt
│   └── stopwords_fr.txt
├── models
│   ├── english_embedding.bin
│   ├── french_embedding.bin
│   ├── synonyms_en.json
│   └── synonyms_fr.json
├── src
│   ├── app.py
│   ├── entity_extraction.py
│   ├── query_expansion.py
│   ├── search.py
│   ├── similarity.py
│   ├── ranking.py
│   ├── language_detection.py
│   ├── third_party_integration.py
│   ├── vector_database.py
│   ├── vectorization.py
│   └── utilities.py
├── templates
│   ├── base.html
│   └── search.html
├── static
│   └── style.css
├── README.md
├── requirements.txt


data: Contains the dataset files for English and French documents, as well as the stopword files for English and French.
models: Contains the trained embedding and synonym files for English and French.
src: Contains the source code for the various components of the search engine, including the main application code, entity extraction, query expansion, search, similarity, ranking, language detection, third-party integration, vector database, vectorization, and utility functions.
templates: Contains the HTML templates for the search engine user interface.
static: Contains the CSS file for the search engine user interface.
README.md: Contains the project description and instructions on how to use the search engine.
requirements.txt: Contains the required libraries and dependencies for the project.
