import os

def get_proj_dir(curr_dir):
    proj_home, curr_dir = str(curr_dir).rsplit('python', 1)
    return proj_home


def get_output_dir(name, output_directory):
    return os.path.join(output_directory, name)


def get_formatted_orig_file_name(sys_path):
    loc = str(sys_path).split(".data")[0]
    path, file = os.path.split(loc)
    file = file.replace("_", "-")
    return file


def get_formatted_gold_file_name(sys_path):
    loc = str(sys_path).split(".gold")[0]
    path, file = os.path.split(loc)
    file = file.replace("_", "-")
    file_name = file.split(".")[0]
    file_num = file.split(".")[1]
    return file_name + "_reference" + file_num + ".txt"