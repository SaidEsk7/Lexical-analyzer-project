import re
import sys
import csv


def main():
    print("--- Lexical Analyzer ---")
    text = input("Enter a sentence or paragraph: ")

    if not text:
        sys.exit("No text provided.")

    tokens = tokenize(text)
    print("\n--- Analysis results ---")
    print(f"Total Words: {count_words(tokens)}")
    print(f"Vocabulary Size (Unique Words): {get_vocabulary_size(tokens)}")
    print(f"Word Frequencies: {get_frequencies(tokens)}")

    frequencies = get_frequencies(tokens)
    export_csv(frequencies)

# Get only valid words ignoring punct and converting text to lowercase


def tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())


def count_words(tokens):
    # Get total length of token list
    return len(tokens)


def get_vocabulary_size(tokens):

    return len(set(tokens))


def get_frequencies(tokens):

    frequencies = {}

    for token in tokens:
        frequencies[token] = frequencies.get(token, 0) + 1
    return frequencies


def export_csv(frequencies):
    with open("frequencies.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Word", "Frequency"])
        for word in frequencies:
            writer.writerow([word, frequencies[word]])
    print("Word frequencies have been exported to 'frequencies.csv'!")


if __name__ == "__main__":
    main()
