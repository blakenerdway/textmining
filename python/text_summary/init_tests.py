import sys
from pathlib import Path
import os
import shutil


def get_output_dir(name, output_directory):
    return output_directory + "/" + name + "/"


def get_formatted_file_name(sys_path):
    loc = str(sys_path).split(".gold")[0]
    file_arr = loc.split("/")
    orig = file_arr[len(file_arr) - 1].replace("_", "-")
    file_name = orig.split(".")[0]
    file_num = orig.split(".")[1]
    return file_name + "_reference" + file_num + ".txt"


if __name__ == "__main__":
    if len(sys.argv) == 1 or len(sys.argv) == 2:
        print("Usage: \"python init_tests <input dir> <output dir for results of system or references>\"")
        sys.exit(1)

    gold_standards_dir = sys.argv[1]
    output_dir = sys.argv[2]

    output_reference = output_dir + "/reference"
    output_system = output_dir + "/system"

    if str(output_dir).endswith("/"):
        split_arr = output_dir.split("/")
        output_results = split_arr[0:len(split_arr) - 2]
    else:
        split_arr = output_dir.split("/")
        output_results = split_arr[0:len(split_arr) - 1]

    output_results = "/".join(output_results) + "/results"

    if not os.path.exists(output_reference):
        os.makedirs(output_reference)
    if not os.path.exists(output_system):
        os.makedirs(output_system)

    if not os.path.exists(output_results):
        os.makedirs(output_results)

    files = Path(gold_standards_dir).glob('**/*.gold')
    for path in files:
        string_path = str(path)
        name = get_formatted_file_name(path)
        print(name)
        shutil.copy(str(path), output_reference + "/" + name)
