from text_summary import summary_gen
import sys
import csv
from pathlib import Path
import io
import time
import os
from text_summary.tests import test_util


class RunTests:
    @staticmethod
    def create_summary(text, impl_name, output_dir, orig_file_name):
        file_name = orig_file_name + "_" + impl_name + ".txt"

        with open(os.path.join(output_dir, file_name), 'w') as text_file:
            summary = summary_gen.summarize(type=impl_name, text=text)
            text_file.write(summary)

    @staticmethod
    def get_file_name(sys_path):
        loc = str(sys_path).split(".txt")[0]
        file_arr = loc.split(os.sep)
        return file_arr[len(file_arr) - 1].replace("_", "-")


def run(data_dir, test_set):
    input_dir = os.path.join(data_loc, "original", test_set)
    output_dir = os.path.join(data_loc, "results", test_set, "system")

    if not os.path.exists(input_dir) or not os.path.exists(output_dir):
        sys.stderr.write("Call init_tests.py first")
        sys.exit(1)

    impl = ["nltk", "gensim", "lexrank", "lsa", "luhn"]

    files = Path(input_dir).glob('**/*.txt')

    with open(os.path.join(data_dir, "results", test_set + '_summary_time.csv'), mode='w') as result_file:
        field_names = ['original_file_name', 'toolkit', 'time_taken']
        result_writer = csv.DictWriter(result_file, fieldnames=field_names)
        result_writer.writeheader()
        for path in files:
            string_path = str(path)
            name = RunTests().get_file_name(path)

            with io.open(string_path, 'r', encoding='windows-1252') as file_text:
                file_str = file_text.read()
                for system in impl:
                    start_time = time.time()
                    try:
                        RunTests().create_summary(file_str, system, output_dir, name)
                        result_writer.writerow({'original_file_name': name,
                                                'toolkit': system,
                                                'time_taken': str(time.time() - start_time)})
                    except Exception:
                        print("Failed to summarize doc: " + name + " using " + system)


if __name__ == "__main__":
    curr_dir = os.getcwd()
    proj_home = test_util.get_proj_dir(curr_dir)
    data_loc = os.path.join(proj_home, "data")

    run(data_loc, test_set='opinions')
    run(data_loc, test_set='news')
