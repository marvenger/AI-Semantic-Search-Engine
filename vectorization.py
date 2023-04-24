#!/usr/bin/env python
# coding: utf-8




import torch
import transformers

class VectorizationAlgorithm:
    def __init__(self, model_name, device):
        """
        Initializes the vectorization algorithm using the specified model name and device.

        Args:
            model_name (str): The name of the pre-trained language model to use for vectorization.
            device (str): The device to use for vectorization (e.g. 'cpu', 'cuda').
        """
        self.tokenizer = transformers.AutoTokenizer.from_pretrained(model_name)
        self.model = transformers.AutoModel.from_pretrained(model_name).to(device)
        self.device = device

    def vectorize(self, text):
        """
        Vectorizes the input text using the pre-trained language model.

        Args:
            text (str): The input text to vectorize.

        Returns:
            torch.Tensor: A tensor representing the vectorized form of the input text.
        """
        # Tokenize the input text and convert to tensor
        inputs = self.tokenizer(text, return_tensors='pt').to(self.device)

        # Pass the input through the pre-trained language model and get the output vector
        with torch.no_grad():
            outputs = self.model(**inputs)
            vector = outputs.last_hidden_state.mean(dim=1).squeeze(0)

        return vector

