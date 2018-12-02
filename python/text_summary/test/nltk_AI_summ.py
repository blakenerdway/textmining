import bs4 as bs
import urllib.request
from  text_summary.nltk_summary import Summarizer

if __name__ == '__main__':
    scraped_data = urllib.request.urlopen('https://en.wikipedia.org/wiki/Artificial_intelligence')
    article = scraped_data.read()

    parsed_article = bs.BeautifulSoup(article, 'lxml')

    paragraphs = parsed_article.find_all('p')

    article_text = ""

    for p in paragraphs:
        article_text += p.text

    summary = '\n'.join(Summarizer().summarize_text(article_text))
    print(summary)
