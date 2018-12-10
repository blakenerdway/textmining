from text_summary import summary_gen
import sys
import csv
from pathlib import Path
import io
import time
import os


class RunTests:
    @staticmethod
    def create_summary(text, impl_name, output_dir, orig_file_name):
        file_name = orig_file_name + "_" + impl_name + ".txt"

        with open(str(output_dir + "/" + file_name), 'w') as text_file:
            summary = summary_gen.summarize(type=impl_name, text=text)
            text_file.write(summary)

    @staticmethod
    def get_file_name(sys_path):
        loc = str(sys_path).split(".txt.data")[0]
        file_arr = loc.split("/")
        return file_arr[len(file_arr) - 1].replace("_", "-")


if __name__ == "__main__":
    if len(sys.argv) == 1 or len(sys.argv) == 2:
        print("Usage: \"python -m text_summary.run_tests <input dir> <output dir>\"")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]

    impl = ["nltk", "gensim", "lexrank", "lsa", "luhn"]

    files = Path(input_dir).glob('**/*.txt.data')

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           'summary_time_results.csv'), mode='w') as result_file:
        field_names = ['original_file_name', 'toolkit', 'time_taken']
        result_writer = csv.DictWriter(result_file, fieldnames=field_names)
        result_writer.writeheader()
        for path in files:
            string_path = str(path)
            name = RunTests().get_file_name(path)

            print(name)
            with io.open(string_path, 'r', encoding='windows-1252') as file_text:
                file_str = file_text.read()
                for system in impl:
                    start_time = time.time()
                    RunTests().create_summary(file_str, system, output_dir, name)
                    result_writer.writerow({'original_file_name': name,
                                            'toolkit': system,
                                            'time_taken': str(time.time() - start_time)})
