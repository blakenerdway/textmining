import os
import csv


def init_dirs(news_file, data_dir, results_dir):
    output_reference = os.path.join(results_dir, 'reference')
    output_system = os.path.join(results_dir, 'system')
    output_orig_news = os.path.join(data_dir, os.path.join('original', 'news'))

    if not os.path.exists(output_reference):
        os.makedirs(output_reference)
    if not os.path.exists(output_system):
        os.makedirs(output_system)
    if not os.path.exists(output_orig_news):
        os.makedirs(output_orig_news)

    with open(news_file, encoding="utf8") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        counter = 0
        for row in csv_reader:
            doc_counter = "doc" + str(counter)
            orig_file = doc_counter + ".txt"
            reference_file = doc_counter + "_reference.txt"
            orig_file_text = row['text']
            reference_file_text = row['ctext']
            counter += 1

            loc = os.path.join(output_reference, reference_file)
            with open(loc, 'w') as summary_file:
                print('writing summary file: ' + reference_file)
                summary_file.write(reference_file_text)

            loc = os.path.join(output_orig_news, orig_file)
            with open(loc, 'w') as orig_text:
                print('writing original file: ' + orig_file)
                orig_text.write(orig_file_text)
