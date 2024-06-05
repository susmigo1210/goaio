"""
File handler
"""

import shutil
import os


class FileHandler:
    def __init__(self):
        self.home = os.path.expanduser('~')
        self.dot_dir_root = os.path.join(self.home, '.config/goaio')
        self.create_root_directory()

    def create_root_directory(self) -> os.path:
        if not os.path.exists(self.dot_dir_root):
            os.makedirs(self.dot_dir_root)
        return self.dot_dir_root

    def test(self):
        print(self.home)
        print(os.path.exists(self.dot_dir_root))


if __name__ == "__main__":
    FileHandler().test()
