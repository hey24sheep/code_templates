# --------------------------------------------------------------------------------------
# Created By  : hey24sheep.com
# Created Date: 11th Feb 2022
# License : MIT
# version = 1.0
#
# Description : A small file read/write helper class for competitive programming
# --------------------------------------------------------------------------------------
from io import StringIO
import sys


class FileReadWriteHelper:

    def __init__(self):
        pass

    # write data to file
    def write_file(self, data, uniq_id=""):
        o = data
        if type(o) != str:
            o = " ".join(data)
        with open(f"output/{uniq_id}_{self.filename}", "w") as f:
            f.write(o)

    # read single file
    # returns : tuple of file_data : filename
    def read_file(self, file):
        ftxt = None
        file_name = file.split("/")[1]
        with open(file, "r") as f:
            ftxt = f.readlines()

        return ftxt, file_name

    # read multiple files
    # returns : dict {filename : file_data}
    def read_files(self, files):
        self.files = files
        self.data = dict()
        for i in range(len(self.files)):
            file = self.files[i]
            ftxt, filename = self.read_file(file)
            self.data[filename] = ftxt

        return self.data

    # read and load file as standard input
    # returns : tuple of file_data : filename
    def read_file_as_stdin(self, file):
        ftxt, file_name = self.read_file(file)
        sys.stdin = StringIO("".join(ftxt))

        return ftxt, file_name

    # read and load multiple files as standard input
    # returns : dict {filename : file_data}
    def read_files_as_stdin(self, files):
        self.files = files
        self.data = dict()
        for i in range(len(self.files)):
            file = self.files[i]
            ftxt, file_name = self.read_file_as_stdin(file)
            self.data[file_name] = ftxt

        return self.data
