import regex as re
from collections import Counter

def find_words_frequency(file_path):
    '''
    This script takes the path of the text file to be processed as input
    and prints the top ten words and also prints their counts in the given text file.
    '''
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()

    # Use `regex`'s findall function
    all_words = re.findall(r'\b\p{L}+\b', text)
    word_frequency = Counter(all_words)
    most_common_words = word_frequency.most_common(10)

    # Print in tabular format
    print(f"{'Word':<15} {'Count':<5}")
    print("-" * 20)
    for word, count in most_common_words:
        print(f"{word:<15} {count:<5}")

def main():
    file_path = input("Enter the path of file : ")
    find_words_frequency(file_path)

if __name__ == "__main__":
    main()
