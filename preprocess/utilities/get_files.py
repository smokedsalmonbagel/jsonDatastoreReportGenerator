import os


def get_files(dir) -> list:
    files = [file for (dirpath, dirnames, filenames) in os.walk(dir) for file in filenames]
    return files
