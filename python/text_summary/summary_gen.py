from .summarizer import nltk_snowball_summarizer as nltk_snowball_sum
from .summarizer import gensim_summarizer as gensim_sum
from .summarizer.sumy import lex_rank_summarizer as sumy_lex_sum
from .summarizer.sumy import lsa_summarizer as sumy_lsa_sum
from .summarizer.sumy import luhn_summarizer as sumy_luhn_sum


def summarize(text="", type="nltk"):
    if type == "nltk":
        return nltk_snowball_sum.Summarizer.summarize_text(text)
    elif type == "gensim":
        return gensim_sum.Summarizer.summarize_text(text)
    elif type == "lexrank":
        return sumy_lex_sum.Summarizer.summarize_text(text)
    elif type == "lsa":
        return sumy_lsa_sum.Summarizer.summarize_text(text)
    elif type == "luhn":
        return sumy_luhn_sum.Summarizer.summarize_text(text)
