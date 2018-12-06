from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem.snowball import SnowballStemmer
import nltk
import re

class Summarizer:

    @staticmethod
    def summarize_text(text):
        stemmer = SnowballStemmer("english")
        stopWords = set(stopwords.words("english"))
        words = word_tokenize(text)

        freq_table = dict()
        for word in words:
            word = word.lower()
            if word in stopWords:
                continue

            word = stemmer.stem(word)

            if word in freq_table:
                freq_table[word] += 1
            else:
                freq_table[word] = 1

        sentences = sent_tokenize(text)
        sentence_value = dict()

        for sentence in sentences:
            for word, freq in freq_table.items():
                if word in sentence.lower():
                    if sentence in sentence_value:
                        sentence_value[sentence] += freq
                    else:
                        sentence_value[sentence] = freq

        sum_value = 0

        for sentence in sentence_value:
            sum_value += sentence_value[sentence]

        average = int(sum_value / len(sentence_value))

        summary = ''

        for sentence in sentences:
            if sentence in sentence_value and sentence_value[sentence] > (1.2 * average):
                summary += " " + sentence

        # Add a space after a , or ending sentence punctuation if there's no space after it already
        rx = r'(?<=[.,?!])(?=[^\s])'

        return re.sub(rx, " ", summary)
