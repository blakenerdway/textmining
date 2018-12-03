import text_summary.summarizer.nltk_summary as nltk_sum


def summarize(text="", type="nltk"):
    if type == "nltk":
        return nltk_sum.Summarizer.summarize_text(text)
