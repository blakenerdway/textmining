from text_summary.tests import test_util
import os
from pathlib import Path
import shutil


def init_dirs(opinions_dir, data_dir, results_dir):
    input_orig_opinions = os.path.join(opinions_dir, "topics")
    gold_reference_dir = os.path.join(opinions_dir, "summaries-gold")
    output_reference = os.path.join(results_dir, 'reference')
    output_system = os.path.join(results_dir, 'system')
    output_orig_opinions = os.path.join(data_dir, os.path.join('original', 'opinions'))

    if not os.path.exists(output_reference):
        os.makedirs(output_reference)
    if not os.path.exists(output_system):
        os.makedirs(output_system)
    if not os.path.exists(output_orig_opinions):
        os.makedirs(output_orig_opinions)

    files = Path(gold_reference_dir).glob('**/*.gold')
    for path in files:
        name = test_util.get_formatted_gold_file_name(path)
        print(name)
        shutil.copy(str(path), os.path.join(output_reference, name))

    files = Path(input_orig_opinions).glob('**/*.txt.data')
    for path in files:
        name = test_util.get_formatted_orig_file_name(path)
        shutil.copy(str(path), os.path.join(output_orig_opinions, name))
