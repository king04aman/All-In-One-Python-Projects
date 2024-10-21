# TextRank-based Text Summarization

This project implements a **TextRank-based approach** to extract summaries from large textual data, such as articles. The summarization algorithm ranks sentences based on their relevance and importance, using concepts derived from the PageRank algorithm applied to text.

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [How It Works](#how-it-works)
5. [Project Structure](#project-structure)
6. [Dependencies](#dependencies)
7. [License](#license)

---

## Features

- Preprocesses text to clean and remove stopwords.
- Utilizes **GloVe word embeddings** for sentence vectorization.
- Applies the **TextRank algorithm** to rank and select important sentences.
- Automatically downloads GloVe embeddings if not present locally.
- Outputs a summary of the most relevant sentences from the input text.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/king04aman/All-In-One-Python-Projects.git
   ```
2. Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. Download necessary NLTK data for tokenization and stopword removal:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   ```

## Usage

1. Prepare your CSV file with a column `article_text` containing the text articles you want to summarize.

2. Run the script with your desired input:
   ```bash
   python text_summarizer.py
   ```

### Example:

- Ensure the input CSV file is in the directory:

  ```bash
  Text Summarizer/sample.csv
  ```

- The script will output the summary of the most important sentences from the input text.

### Command-line Parameters

You can modify the following paths and settings inside the script:

- `input_csv`: Path to your input CSV file.
- `glove_dir`: Directory for storing GloVe embeddings.
- `glove_file`: Path to the GloVe embeddings file.
- `top_n_sentences`: The number of sentences you want in the summary (default is 10).

## How It Works

### 1. Text Preprocessing

- Sentences are tokenized, and each sentence is cleaned by:
  - Removing punctuation, numbers, and special characters.
  - Converting text to lowercase.
  - Removing stopwords using the NLTK library.

### 2. Sentence Vectorization

- The script uses **GloVe embeddings** to convert words in each sentence into a vector representation. Sentence vectors are the average of all word vectors in a sentence.
- If the embeddings are not present, the script automatically downloads them.

### 3. Building Similarity Matrix

- A similarity matrix is built by calculating the **cosine similarity** between sentence vectors. This matrix forms the basis for ranking sentences.

### 4. Sentence Ranking

- The **PageRank algorithm** is applied to the similarity matrix. Sentences are ranked based on their scores, where higher-ranked sentences are deemed more important for summarization.

### 5. Output Summary

- Based on the rankings, the top `n` sentences are selected as the summary. These sentences are printed as the output of the script.

## Project Structure

```
.
├── Text Summarizer/
│   ├── sample.csv                # Example CSV input file with articles
│   ├── text_summarizer.py  # Main script for summarization
│   ├── glove/                    # Directory for storing GloVe embeddings
│   └── text_summarizer.log # Log file
```

## Dependencies

- **Python 3.x**
- **Libraries**:
  - `numpy`
  - `pandas`
  - `nltk`
  - `sklearn`
  - `networkx`
  - `requests`
  - `tqdm`

All dependencies can be installed via:

```bash
pip install -r requirements.txt
```

### GloVe Embeddings

- The script uses **GloVe embeddings** from Stanford NLP to generate sentence vectors.
  - By default, the **100-dimensional GloVe vectors** (`glove.6B.100d.txt`) are used.
  - Download link: [GloVe 6B embeddings](http://nlp.uoregon.edu/download/embeddings/glove.6B.100d.txt)

## Short Summary

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

Author: [Himanshu Mahajan](https://github.com/himanshumahajan138)

Date: 19-10-2024


## License

This project is licensed under the MIT License.

---
