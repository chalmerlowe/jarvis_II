# TITLE: interleave >> your_code_here_interleave.py
# AUTHOR: Chalmer Lowe
# DESCRIPTION:

# You are given a file (interleave.txt) with two lines.

# Each line contains numbers separated by semicolons.
# You will need to interleave the values from the two lines and calculate
#     the difference between each sequential pair of numbers.
# Sum all the even differences.

# For example... given the following numbers...

#     a = [1, 4, 9]
#     b = [8, 3, 3]

# interleaved_nums = [1,  8,  4,  3,  9,  3]
#                     ^   ^   ^   ^   ^   ^
#                    a1, b1, a2, b2, a3, b3

# If we examine, sequentially, all pairs of values to find any pairs that have
#     a difference between them that is even:

# between a1 and b1: 1 - 8 = -7   which is an odd difference
# between b1 and a2: 8 - 4 = 4    which is an even difference
# between a2 and b2: 4 - 3 = 1    which is odd
# between b2 and a3: 3 - 9 = -6   which is even
# between a3 and b3: 9 - 3 = 6    which is even

# Adding all the even differences yields:
#     4 + -6 + 6 = 4

# Answer = 4

# ==============================================================
import functools

def interleave_lists(a,b):
    interleaved = []
    if len(a) != len(b):
        raise(ValueError)
    for i in range(len(a)):
        interleaved.append(a[i])
        interleaved.append(b[i])

    return interleaved
    
def get_even_differences(l):
    def is_even(item):
        return (item % 2) == 0

    diffs = []
    even_diffs = []
    
    for i in range(1,len(l)):    
        diffs.append(l[i-1] - l[i])
    
    even_diffs = list(filter(is_even, diffs))
    
    return even_diffs
    
def get_lists():
    with open('interleave.txt','r') as f:
        a = [int(n) for n in f.readline().strip().split(';')]        
        b = [int(n) for n in f.readline().strip().split(';')]        
    return a,b

def main():
    a,b = get_lists()
    print("a =", a)
    print("b =", b)
    interleaved  = interleave_lists(a,b)
    print ("interleaved =",interleaved)
    diffs = get_even_differences(interleaved)
    print("diffs =",diffs)
    print("answer =",functools.reduce(lambda x,y: x+y, diffs))

main()            
######################        
import unittest

class TestInterleave(unittest.TestCase):
    a = [1, 4, 9]
    b = [8, 3, 3]

    interleaved_nums = [1,  8,  4,  3,  9,  3]
    even_differences = [4, -6,  6]
    
    def test_interleaved_number(self):
        self.assertEqual(interleave_lists(self.a,self.b), self.interleaved_nums)
        
    def test_even_differences(self):
        self.assertEqual(get_even_differences(self.interleaved_nums),self.even_differences)
    
    def test_final_answer(self):
        diffs = get_even_differences(self.interleaved_nums)
        evendiffsum = functools.reduce(lambda x,y: x+y, diffs)
        self.assertEqual(evendiffsum, 4)
        # Answer = 4
        
if __name__ == '__main__':
    unittest.main()
