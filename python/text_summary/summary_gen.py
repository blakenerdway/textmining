import text_summary.summarizer.nltk_summary as nltk_sum
import text_summary.summarizer.nltk_snowball_summarizer as nltk_snowball_sum


def summarize(text="", type="nltk"):
    print(type)
    if type == "nltk":
        return nltk_snowball_sum.Summarizer.summarize_text(text)
    elif type == "gensim":
        return nltk_snowball_sum.Summarizer.summarize_text(text)
