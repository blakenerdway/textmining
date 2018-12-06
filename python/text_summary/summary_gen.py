import text_summary.summarizer.nltk_snowball_summarizer as nltk_snowball_sum
import text_summary.summarizer.gensim_summarizer as gensim_sum
import text_summary.summarizer.sumy.lex_rank_summarizer as sumy_lex_sum
import text_summary.summarizer.sumy.lsa_summarizer as sumy_lsa_sum
import text_summary.summarizer.sumy.luhn_summarizer as sumy_luhn_sum


def summarize(text="", type="nltk"):
    if type == "nltk":
        return nltk_snowball_sum.Summarizer.summarize_text(text)
    elif type == "gensim":
        return gensim_sum.Summarizer.summarize_text(text)
    elif type == "sumy.lexrank":
        return sumy_lex_sum.Summarizer.summarize_text(text)
    elif type == "sumy.lsa":
        return sumy_lsa_sum.Summarizer.summarize_text(text)
    elif type == "sumy.luhn":
        return sumy_luhn_sum.Summarizer.summarize_text(text)
