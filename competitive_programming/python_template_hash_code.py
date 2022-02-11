# --------------------------------------------------------------------------------------
# Created By  : hey24sheep.com
# Created Date: 11th Feb 2022
# License : MIT
# version = 1.0
#
# Description : A small and quick template file for competitve programming
# --------------------------------------------------------------------------------------
import sys, io, os, math, bisect
from io import StringIO
from collections import Counter, defaultdict, OrderedDict, deque
from itertools import permutations, combinations
from sys import stdin, stdout
import random

# set max recurssion limit
sys.setrecursionlimit(100000000)
# 10**9+7 prime
mod = 1000000007


class IOHelper:

    def __init__(self) -> None:
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

    # input_problem_idx : to process a single problem statment
    def read_files(self, input_problem_list, input_problem_idx=-1):
        if input_problem_idx > -1:
            self.file_data = self.read_files_as_stdin(
                input_problem_list[input_problem_idx])
        else:
            self.file_data = self.read_files_as_stdin(input_problem_list)
        return self.file_data

    def process_inputs(self, input_problem_list, input_problem_idx=-1):
        data = self.read_files(input_problem_list, input_problem_idx)

        # process input normally from here, like so
        # n = int(input())

        pass
        # return processed_data


class Solver(IOHelper):

    def __init__(self, input_problem_list, input_problem_idx=-1) -> None:
        # constructor
        # (var1, var1,) = self.process_inputs(input_problem_list, input_problem_idx)
        pass

    def solve(self):
        # write solver here
        pass


class Scorer(IOHelper):

    def __init__(self, ) -> None:
        pass

    def solve(self):
        # write simulator/scorer here
        pass

    def solve_n_times(self):
        # uncomment, if need
        # ite = 1
        # p_data
        # while(ite > 0):
        #     p_data = self.solve()
        #     ite -= 1
        # return p_data
        pass

def main():
    # input_files = [
    #     'input/a.problem.txt'
    # ]
    # solver = Solver(input_files)
    # scorer = Scorer()

    return


main()
