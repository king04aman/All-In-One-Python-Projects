"""
TextRank Text Summarization

This script implements a TextRank-based approach for text summarization.
The input is a CSV file containing text articles, and the output is a summary
of the text.

Steps:
1. Preprocesses the text by removing punctuation, numbers, special characters, and stopwords.
2. Generates sentence vectors using GloVe word embeddings.
3. Builds a similarity matrix using cosine similarity between sentence vectors.
4. Applies the PageRank algorithm to rank sentences.
5. Outputs a summary of the most important sentences.

Dependencies:
- numpy
- pandas
- nltk
- sklearn
- networkx
- GloVe word embeddings (automatically downloaded if not present)

Author: Himanshu Mahajan (GitHub: himanshumahajan138)
Date: 19-10-2024
"""

import os
import requests
from tqdm import tqdm
import numpy as np
import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("Text Summarizer/text_summarizer.log"),
        logging.StreamHandler(),
    ],
)

# Download necessary NLTK data (if not already available)
nltk.download("punkt")  # Sentence tokenizer
nltk.download("stopwords")  # Stopwords list


# Function to preprocess and clean sentences
def preprocess_sentences(sentences):
    """
    Cleans and preprocesses sentences by removing non-alphabetic characters,
    converting to lowercase, and removing stopwords.

    Args:
        sentences (list): List of sentences.

    Returns:
        list: Cleaned and preprocessed sentences.
    """
    logging.info("Preprocessing sentences...")
    # Remove punctuation, numbers, and special characters
    clean_sentences = pd.Series(sentences).str.replace("[^a-zA-Z]", " ", regex=True)

    # Convert to lowercase
    clean_sentences = [s.lower() for s in clean_sentences]

    # Remove stopwords
    stop_words = stopwords.words("english")
    clean_sentences = [
        " ".join([word for word in sentence.split() if word not in stop_words])
        for sentence in clean_sentences
    ]

    logging.info("Preprocessing completed.")
    return clean_sentences


# Function to generate sentence vectors using GloVe embeddings
def generate_sentence_vectors(sentences, word_embeddings, embedding_dim=100):
    """
    Converts sentences into vectors by averaging the GloVe word embeddings of each word in the sentence.

    Args:
        sentences (list): List of sentences.
        word_embeddings (dict): GloVe word embeddings.
        embedding_dim (int): Dimensionality of GloVe vectors.

    Returns:
        list: List of sentence vectors.
    """
    logging.info("Generating sentence vectors...")
    sentence_vectors = []
    for sentence in sentences:
        if len(sentence) != 0:
            words = sentence.split()
            sentence_vector = sum(
                [
                    word_embeddings.get(word, np.zeros((embedding_dim,)))
                    for word in words
                ]
            ) / (len(words) + 0.001)
        else:
            sentence_vector = np.zeros((embedding_dim,))
        sentence_vectors.append(sentence_vector)

    logging.info("Sentence vectors generated.")
    return sentence_vectors


# Function to build similarity matrix
def build_similarity_matrix(sentence_vectors):
    """
    Builds a similarity matrix using cosine similarity between sentence vectors.

    Args:
        sentence_vectors (list): List of sentence vectors.

    Returns:
        np.ndarray: Similarity matrix.
    """
    logging.info("Building similarity matrix...")
    sim_mat = np.zeros([len(sentence_vectors), len(sentence_vectors)])

    for i in range(len(sentence_vectors)):
        for j in range(len(sentence_vectors)):
            if i != j:
                sim_mat[i][j] = cosine_similarity(
                    sentence_vectors[i].reshape(1, -1),
                    sentence_vectors[j].reshape(1, -1),
                )[0, 0]

    logging.info("Similarity matrix built.")
    return sim_mat


# Function to rank sentences using TextRank algorithm
def rank_sentences(similarity_matrix, sentences, top_n=10):
    """
    Ranks sentences based on the PageRank algorithm applied to the similarity matrix.

    Args:
        similarity_matrix (np.ndarray): Similarity matrix.
        sentences (list): List of original sentences.
        top_n (int): Number of top-ranked sentences to return.

    Returns:
        list: Top-ranked sentences.
    """
    logging.info(f"Ranking top {top_n} sentences...")
    nx_graph = nx.from_numpy_array(similarity_matrix)
    scores = nx.pagerank(nx_graph)

    ranked_sentences = sorted(
        ((scores[i], sentence) for i, sentence in enumerate(sentences)), reverse=True
    )

    logging.info("Sentences ranked.")
    return [ranked_sentences[i][1] for i in range(top_n)]


# Function to download and extract GloVe embeddings
def download_glove(glove_url, glove_file, glove_dir):
    """
    Downloads and extracts GloVe embeddings if not already present.

    Args:
        glove_url (str): URL to the GloVe embeddings zip file.
        glove_zip (str): Path to the GloVe zip file.
        glove_dir (str): Directory where the GloVe files will be extracted.
    """
    if not os.path.exists(glove_file):
        os.makedirs(glove_dir, exist_ok=True)
        logging.info("GloVe embeddings not found, downloading...")

        # Stream the request to handle large files
        with requests.get(glove_url, stream=True) as response:
            response.raise_for_status()
            total_size = int(response.headers.get("content-length", 0))
            block_size = 1024  # 1 Kibibyte

            # Use tqdm to show progress bar
            with tqdm(
                total=total_size, unit="B", unit_scale=True, desc=glove_file
            ) as progress_bar:
                with open(glove_file, "wb") as file:
                    for data in response.iter_content(block_size):
                        file.write(data)
                        progress_bar.update(len(data))

        logging.info("Download complete. Extracting files...")

    else:
        logging.info("GloVe embeddings already present.")


# Main function to summarize text using TextRank
def summarize_text(input_csv, glove_file, top_n=10):
    """
    Summarizes the text from a CSV file using the TextRank algorithm.

    Args:
        input_csv (str): Path to the input CSV file.
        glove_file (str): Path to the GloVe embeddings file.
        top_n (int): Number of sentences to include in the summary.

    Returns:
        list: Summary sentences.
    """
    logging.info(f"Starting text summarization for {input_csv}...")

    # Read the CSV file
    df = pd.read_csv(input_csv)

    # Tokenize articles into sentences
    logging.info("Tokenizing articles into sentences...")
    sentences = [sent_tokenize(article) for article in df["article_text"]]
    sentences = [
        sentence for sublist in sentences for sentence in sublist
    ]  # Flatten the list

    # Preprocess sentences
    clean_sentences = preprocess_sentences(sentences)

    # Load GloVe embeddings
    logging.info("Loading GloVe embeddings...")
    word_embeddings = {}
    with open(glove_file, "r", encoding="utf-8") as f:
        for line in f:
            values = line.split()
            word = values[0]
            coefs = np.asarray(values[1:], dtype="float32")
            word_embeddings[word] = coefs

    # Generate sentence vectors
    sentence_vectors = generate_sentence_vectors(clean_sentences, word_embeddings)

    # Build similarity matrix
    sim_mat = build_similarity_matrix(sentence_vectors)

    # Rank sentences
    summary = rank_sentences(sim_mat, sentences, top_n=top_n)

    logging.info(f"Text summarization completed for {input_csv}.")
    return summary


if __name__ == "__main__":
    # Define paths and parameters
    input_csv = os.getcwd() + "/Text Summarizer/sample.csv"  # Path to input CSV file
    glove_dir = "Text Summarizer/glove"  # Directory where GloVe files will be stored

    glove_file = os.path.join(
        os.getcwd(), glove_dir, "glove.6B.100d.txt"
    )  # Path to GloVe embeddings file

    glove_url = "http://nlp.uoregon.edu/download/embeddings/glove.6B.100d.txt"  # URL for GloVe embeddings

    top_n_sentences = 10  # Number of sentences in the summary

    # Download and extract GloVe embeddings
    download_glove(glove_url, glove_file, glove_dir)

    # Generate summary
    summary = summarize_text(input_csv, glove_file, top_n_sentences)

    # Print summary
    print("Summary:")
    for sentence in summary:
        print(sentence + "\n")
