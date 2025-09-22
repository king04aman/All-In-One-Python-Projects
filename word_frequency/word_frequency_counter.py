from collections import Counter

def count_words(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read().lower().split()
    word_counts = Counter(text)
    for word, count in word_counts.most_common(10):
        print(f"{word}: {count}")

if __name__ == "__main__":
    count_words("counter_sample.txt")
