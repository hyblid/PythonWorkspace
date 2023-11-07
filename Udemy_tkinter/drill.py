# from brank.hello import print_hello
# import sys
# sys.path.append(r"D:\test\PythonWorkspace")
# from python_challenges.array_utils import print_array

from ..python_challenges.array_utils import print_array

values = [
        ['1', '2', '3', '4', '5'],
        ['J', 'K', 'L', 'M', 'N'],
        ['I', 'V', 'W', 'X', 'O'],
        ['H', 'U', 'Z', 'Y', 'P'],
        ['G', 'T', 'S', 'R', 'Q'],
        ['F', 'E', 'D', 'C', 'B']]


board = [[0 for x in range(7)] for y in range(5)]
print_array(board)
