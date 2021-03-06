from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.nlp.stemmers import Stemmer
import sumy.utils


class Summarizer:
    @staticmethod
    def summarize_text(text):
        language = "english"

        parser = PlaintextParser.from_string(text, Tokenizer(language))

        summarizer = LuhnSummarizer(Stemmer(language))
        summarizer.stop_words = sumy.utils.get_stop_words(language)
        summary_text = ""
        for sentence in summarizer(parser.document, 5):
            summary_text += str(sentence) + " "

        return summary_text
