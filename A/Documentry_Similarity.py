import os
from collections import Counter
import math

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def tokenize(text):
    return text.split()

def calculate_tf_vector(tokens):
    return dict(Counter(tokens))

def dot_product(v1, v2):
    return sum(v1.get(term, 0) * v2.get(term, 0) for term in set(v1) | set(v2))

def magnitude(v):
    return math.sqrt(sum(v[i] ** 2 for i in v))

def cosine_similarity(v1, v2):
    return dot_product(v1, v2) / (magnitude(v1) * magnitude(v2))

def document_similarity(query_vector, document_vectors):
    similarities = []
    for i, doc_vector in enumerate(document_vectors):
        similarity = cosine_similarity(query_vector, doc_vector)
        similarities.append((i+1, similarity))
    return sorted(similarities, key=lambda x: x[1], reverse=True)

def main():
    query_file_path = input("Enter the query file path: ")

    document_file_paths = []
    for i in range(2):
        document_file_paths.append(input(f"Enter the file path for document {i+1}: "))

    try:
        # Read query text
        query_text = read_file(query_file_path)

        document_texts = [read_file(file_path) for file_path in document_file_paths]

        query_tokens = tokenize(query_text)
        document_tokens = [tokenize(doc_text) for doc_text in document_texts]

        query_vector = calculate_tf_vector(query_tokens)
        document_vectors = [calculate_tf_vector(tokens) for tokens in document_tokens]

        similarities = document_similarity(query_vector, document_vectors)

        for doc_num, similarity in similarities:
            print(f"Document {doc_num}: Similarity Score = {similarity:.2f}")

    except FileNotFoundError as e:
        print(f"Error: {e.filename} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

