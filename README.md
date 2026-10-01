# Lexical Tokenizer & Word-Frequency Analyzer

## Overview & Academic Context
This repository contains my final project for Harvard University's CS50P (Introduction to Programming with Python). It serves as my foundational entry into Computational Linguistics, demonstrating the ability to parse, normalize, and analyze natural language data using core programming constructs. 

Rather than relying on high-level NLP abstractions like NLTK or spaCy, this project was  built using pure Python to prove a fundamental understanding of underlying data structures, text normalization, and algorithmic logic.

## Core Functionality
The program acts as a rudimentary lexical analyzer. It ingests raw text, processes the data, and outputs a structured frequency distribution of the vocabulary.

*   **Text Normalization:** Converts all input to lowercase to ensure case-insensitive processing.
*   **Tokenization:** Utilizes regular expressions (`re`) to strip punctuation, whitespace, and non-alphanumeric characters, cleanly isolating valid word tokens.
*   **Frequency Mapping:** Iterates through the tokenized list using nested logic and dictionaries to build a quantitative map of word occurrences.

## Sample Output
```text
$ python analyzer.py
Input text to analyze: The quick brown fox jumps over the lazy dog. The dog barks.

--- Lexical Analysis Results ---
Total Words Processed: 12
Unique Vocabulary Size: 9

Frequency Distribution:
 -> the: 3
 -> dog: 2
 -> quick: 1
 -> brown: 1
 -> fox: 1
 -> jumps: 1
 -> over: 1
 -> lazy: 1
 -> barks: 1
