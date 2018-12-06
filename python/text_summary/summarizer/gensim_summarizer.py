from gensim.summarization import summarize
import re


class Summarizer:
    @staticmethod
    # Returns a summary defaulted to 20% the size of the original (see gensim.summarization `summarize` default params)
    def summarize_text(text):
        return summarize(text, ratio=0.1)
