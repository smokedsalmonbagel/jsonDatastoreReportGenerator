import os


def get_files() -> list:
    rootDir = "logs"
    files = [os.path.relpath(os.path.join(dirpath, file), rootDir) for (
        dirpath, dirnames, filenames) in os.walk(rootDir) for file in filenames]
    return files
