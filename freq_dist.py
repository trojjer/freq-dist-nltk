# Marc Kirkwood, 2020.
# Frequency analysis of words found in input text documents, with example sentence contexts.
# Excludes English stop words.

from typing import Sequence, Mapping, List
from glob import glob
from csv import DictWriter

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords


STOP_WORDS = set(stopwords.words('english'))


def analyse_documents(file_paths: Sequence[str], top_n_words: int = 20) -> List[dict]:
    """
    Reads the contents of each file given and outputs frequency distribution and example sentence context data
    for the most common words.
    :param file_paths: Paths of input text files.
    :param top_n_words: Default is 20, i.e. top 20 words by frequency.
    :return output_data: List of output rows as dicts.
    """
    document_words = {}
    all_doc_words = []
    all_doc_sentences = []
    for file_path in file_paths:
        with open(file_path) as in_file:
            text = in_file.read()
            all_doc_sentences.extend(sent_tokenize(text))
            words = word_tokenize(text.lower())
            filtered_words = [w for w in words if w.isalnum() and w not in STOP_WORDS]
            document_words[file_path.split('data/')[1]] = filtered_words
            all_doc_words.extend(filtered_words)

    frequency_dist = FreqDist(all_doc_words)
    top_words = frequency_dist.most_common(top_n_words)
    output_data = []
    for word, frequency in top_words:
        doc_names = [f for f, words in document_words.items() if word in words]
        example_sentences = find_concordant_sentences(word, all_doc_sentences)
        output_data.append({
            'Word': word,
            'Frequency': frequency,
            'Documents': '\n'.join(doc_names),
            'Example sentences': '\n'.join(example_sentences),
        })
    return output_data


def find_concordant_sentences(token: str, sentences: Sequence[str], matches: int = 2) -> List[str]:
    """
    Returns concordant sentences for a given token word, providing surrounding context.
    :param token: Word to find.
    :param sentences: Sequence of sentences to check.
    :param matches: Number of matching sentences to find (default 2).
    :return matching_sentences:
    """
    matching_sentences = []
    for sentence in sentences:
        words = word_tokenize(sentence.lower())
        if len(matching_sentences) < matches:
            if token in words:
                matching_sentences.append(sentence)
        else:
            break
    return matching_sentences


def write_output(output_data: Sequence[Mapping], file_path: str):
    """
    Write output to CSV.
    :param output_data: Sequence of mappings for each output row.
    :param file_name: Destination CSV file path.
    """
    with open(file_path, 'w', newline='') as out_file:
        writer = DictWriter(out_file, fieldnames=output_data[0].keys())
        writer.writeheader()
        writer.writerows(output_data)


if __name__ == '__main__':
    file_names = glob('data/*.txt')
    top_n_words = 20
    output_data = analyse_documents(file_names, top_n_words)
    out_file_name = f'top_{top_n_words}_words.csv'
    print(f'Writing results for top word frequencies to {out_file_name}...')
    write_output(output_data, out_file_name)
    print('Complete.')
