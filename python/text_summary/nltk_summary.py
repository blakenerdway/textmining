import nltk
import re
import heapq


class Summarizer:
    text_to_summarize = ""
    formatted_text = ""

    def summarize_text(self, text):

        # Removing Square Brackets and Extra Spaces
        text = re.sub(r'\[[0-9]*\]', ' ', text)
        text = re.sub(r'\s+', ' ', text)

        # Removing special characters and digits
        formatted_article_text = re.sub('[^a-zA-Z]', ' ', text)
        formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

        sentence_list = nltk.sent_tokenize(text)

        stopwords = nltk.corpus.stopwords.words('english')

        word_frequencies = {}

        for w in nltk.word_tokenize(formatted_article_text):
            if w not in stopwords:
                if w not in word_frequencies.keys():
                    word_frequencies[w] = 1
                else:
                    word_frequencies[w] += 1

        max_frequency = max(word_frequencies.values())

        for w in word_frequencies.keys():
            word_frequencies[w] = (word_frequencies[w] / max_frequency)

        sentence_scores = {}
        for sent in sentence_list:
            for word in nltk.word_tokenize(sent.lower()):
                if word in word_frequencies.keys():

                    if len(sent.split(' ')) < 40:
                        if sent not in sentence_scores.keys():
                            sentence_scores[sent] = word_frequencies[word]
                        else:
                            sentence_scores[sent] += word_frequencies[word]

        return heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
