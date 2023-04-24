#!/usr/bin/env python
# coding: utf-8



import pinecone

class VectorDatabase:
    def __init__(self, name, dim):
        """
        Initializes the Pinecone vector database with the given name and dimensionality.

        Args:
            name (str): The name of the vector database.
            dim (int): The dimensionality of the vectors to be stored in the database.
        """
        self.name = name
        self.dim = dim
        self.db = pinecone.Index(name=self.name, dimension=self.dim)

    def insert_documents(self, documents):
        """
        Inserts a list of documents into the vector database.

        Args:
            documents (list): A list of dictionaries, where each dictionary contains a "text" key with the document text.
        """
        for i, doc in enumerate(documents):
            self.db.upsert(ids=[str(i)], vectors=[doc["vector"]])

    def search(self, query, top_k=10):
        """
        Searches the vector database for the most similar documents to the given query.

        Args:
            query (list): A list of floats representing the vectorized query.
            top_k (int): The number of results to return.

        Returns:
            A list of dictionaries, where each dictionary contains the document ID and score.
        """
        results = self.db.query(queries=[query], top_k=top_k)
        return [{"id": r[0], "score": r[1]} for r in results[0]]

