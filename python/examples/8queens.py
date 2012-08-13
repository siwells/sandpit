# Source: http://www.reddit.com/r/tinycode/comments/wgf8m/8_queens_in_6_lines_of_python/

from itertools import permutations

n = 8
cols = range(n)
for vec in permutations(cols):
    if (n == len(set(vec[i]+i for i in cols))
          == len(set(vec[i]-i for i in cols))):
        print vec