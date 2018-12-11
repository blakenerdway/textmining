from text_summary.tests import test_util
import os
from text_summary.tests import init_opinions_dir
from text_summary.tests import init_news_dir
import zipfile
import shutil

if __name__ == "__main__":

    # initialize the directories
    curr_dir = os.getcwd()
    proj_home = test_util.get_proj_dir(curr_dir)
    data_loc = os.path.join(proj_home, "data")

    summaries_dir = os.path.join(data_loc, "opinion-dataset")

    # unzip the data if it hasn't been unzipped already
    if not os.path.exists(summaries_dir):
        with zipfile.ZipFile(os.path.join(data_loc, 'OpinosisDataset1.0_0.zip'), 'r') as zip_ref:
            zip_ref.extractall(summaries_dir)

    # create strings for the output directories
    opinion_output_dir = os.path.join(data_loc, "results", "opinions")
    news_output_dir = os.path.join(data_loc, "results", "news")
    news_input_dir = os.path.join(data_loc, "news-summaries.csv")

    # create the directories and copy the data to whatever files they should go to
    init_opinions_dir.init_dirs(summaries_dir, data_loc, opinion_output_dir)
    init_news_dir.init_dirs(news_input_dir, data_loc, news_output_dir)

    if os.path.exists(summaries_dir):
        shutil.rmtree(summaries_dir)
