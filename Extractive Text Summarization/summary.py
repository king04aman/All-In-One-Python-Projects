import os
import re
import heapq
import numpy as np
from collections import defaultdict
from typing import List, Dict, Tuple, Union
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import spacy
from nltk.stem import PorterStemmer


class TextSummarization:
    def __init__(self):
        try:
            self.nlp = spacy.load('en_core_web_sm')
        except OSError:
            print("Downloading spaCy model...")
            os.system("python -m spacy download en_core_web_sm")
            self.nlp = spacy.load('en_core_web_sm')

        self.tfidf_vectorizer = TfidfVectorizer(stop_words='english')
        self.stemmer = PorterStemmer()

    def clean_text(self, text: str) -> Tuple[str, str]:
        """Clean and preprocess the text, returning both original and stemmed versions."""
        text = re.sub(r'[^\w\s.,!?]', '', text)  # Keep sentence structure
        cleaned_text = ' '.join(text.split())  # Remove extra whitespace
        stemmed_text = self.stem_text(cleaned_text)
        return cleaned_text, stemmed_text

    def stem_text(self, text: str) -> str:
        """Stem the words in the text."""
        words = text.split()
        stemmed_words = [self.stemmer.stem(word) for word in words]
        return ' '.join(stemmed_words)

    def score_sentences(self, original_sentences: List[str], stemmed_sentences: List[str]) -> Dict[str, float]:
        """Score sentences based on TF-IDF and structural features."""
        tfidf_matrix = self.tfidf_vectorizer.fit_transform(stemmed_sentences)
        sentence_scores = defaultdict(float)

        for i, original_sentence in enumerate(original_sentences):
            score = sum(tfidf_matrix[i, j] for j in tfidf_matrix[i].indices)
            sent_doc = self.nlp(original_sentence)

            # Apply length and positional weighting
            length_factor = min(
                1.0, len(sent_doc) / 20.0) if len(sent_doc) < 20 else 20.0 / len(sent_doc)
            score *= length_factor

            # Position bonuses
            if i < len(original_sentence) * 0.2:
                score *= 1.2
            elif i > len(original_sentence) * 0.8:
                score *= 1.1

            # Bonuses for named entities and important dependencies
            if sent_doc.ents:
                score *= 1.2
            if any(token.dep_ in ['nsubj', 'dobj'] for token in sent_doc):
                score *= 1.1

            sentence_scores[original_sentence] = score

        return sentence_scores

    def extract_key_points(self, original_sentences: List[str], stemmed_sentences: List[str], num_clusters: int = 5) -> List[str]:
        """Extract key points using K-means clustering."""
        num_clusters = min(num_clusters, len(original_sentences))
        if num_clusters < 1:
            return []

        tfidf_matrix = self.tfidf_vectorizer.fit_transform(stemmed_sentences)
        kmeans = KMeans(n_clusters=num_clusters, random_state=42)
        kmeans.fit(tfidf_matrix)

        labeled_sentences = [(orig, stem, label, idx) for idx, (orig, stem, label) in enumerate(
            zip(original_sentences, stemmed_sentences, kmeans.labels_))]
        key_points = []

        for cluster in range(num_clusters):
            cluster_sentences = [
                item for item in labeled_sentences if item[2] == cluster]
            if cluster_sentences:
                cluster_center = kmeans.cluster_centers_[cluster]
                distances = [np.linalg.norm(tfidf_matrix[item[3]].toarray(
                ) - cluster_center) for item in cluster_sentences]
                closest_sentence = cluster_sentences[np.argmin(
                    distances)][0]  # Use original sentence

                sent_doc = self.nlp(closest_sentence)
                if len(sent_doc) >= 5:
                    point = re.sub(r'\s+', ' ', closest_sentence.strip('., '))
                    if len(point.split()) >= 5:
                        # Store with original index
                        key_points.append((point, cluster_sentences[0][3]))

        # Sort key points based on their original position in the text
        key_points.sort(key=lambda x: x[1])
        return [point for point, _ in key_points]

    def summarize(self, text: str, num_sentences: int = 5) -> Dict[str, Union[str, List[str]]]:
        """Generate a comprehensive summary of the text."""
        cleaned_text, stemmed_text = self.clean_text(text)
        original_sentences = sent_tokenize(cleaned_text)
        stemmed_sentences = sent_tokenize(stemmed_text)
        num_sentences = min(num_sentences, len(
            original_sentences)) if original_sentences else 0

        sentence_scores = self.score_sentences(
            original_sentences, stemmed_sentences)
        summary_sentences = heapq.nlargest(
            num_sentences, sentence_scores.items(), key=lambda x: x[1])
        summary_sentences.sort(key=lambda x: original_sentences.index(x[0]))

        summary = ' '.join([sentence for sentence, _ in summary_sentences])
        key_points = self.extract_key_points(
            original_sentences, stemmed_sentences, num_clusters=min(5, len(original_sentences)))

        return {
            'summary': summary,
            'key_points': key_points,
        }


def main(text):
    # Create summarizer instance
    summarizer = TextSummarization()

    # Generate summary
    summary = summarizer.summarize(text)

    print("Summary : ")
    print(summary['summary'])
    
    
    print("------\n")
    
    print("Key Points : ")
    for i,j in enumerate(summary["key_points"]):
        print(f"{i+1}. {j}")
        
    print("------")
    


if __name__ == "__main__":
    main("""NLP is a subfield of computer science and artificial intelligence concerned with interactions between computers and human (natural) languages. It is used to apply machine learning algorithms to text and speech.

For example, we can use NLP to create systems like speech recognition, document summarization, machine translation, spam detection, named entity recognition, question answering, autocomplete, predictive typing and so on.

Nowadays, most of us have smartphones that have speech recognition. These smartphones use NLP to understand what is said. Also, many people use laptops which operating system has a built-in speech recognition.""")
