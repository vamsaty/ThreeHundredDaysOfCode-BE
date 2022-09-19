from xml.etree.ElementPath import xpath_tokenizer
from Solution import Solution
import sys
import os

file1 = open(os.path.join(sys.path[0], '../testcases.txt'), 'r')
Lines = file1.readlines()
input = []
x = []
actual_output = []
expected_output = []
status = 0
obj = Solution()
for line in Lines:
    if (line.strip() == "input"):
        status = 1
        continue
    if (line.strip() == "output"):
        status = 0
        continue
    if (line.strip() == "check"):
        actual_output = obj.maximumWealth(input)
        if (expected_output != actual_output):
            print('Result: Failed')
            print("Input: land= {}".format(x))
            print("Actual Output:", actual_output)
            print("Expected Outuput:", expected_output)
            status = 1
            break
        input.clear()
        x.clear()
    if (status == 1 and line.strip() != "check"):
        new_vec = list(map(int, line.split()))
        input.append(new_vec)
        x.append(new_vec.copy())

    if(status == 0 and line.strip() != "check"):
        expected_output = int(line.strip())


if status == 0:
    print('Result: Success')