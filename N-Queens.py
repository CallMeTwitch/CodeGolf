# #########################
# The N-Queens problem is 
# as follows. Find all 
# configurations of N 
# queens on an NxN 
# chessboard so that 
# no queen can take another.
# This output's under the 
# correct ssumption that 
# there will be one queen 
# on every row. Requires 
# input without prompt.
#  
# Output:
# [0, 4, 7, 5, 2, 6, 1, 3] 
# means one queen will be on 
# coordinates (0, 0), (1, 4), 
# (2, 7), (3. 5), (4, 2), 
# (5, 6), (6, 1) and (7, 3).
#
# Code written for Code 
# Golf (As short as 
# possible).
# #########################

from itertools import*;q=range(int(input()));exit([b for b in permutations(q)if all(abs(b[x]-b[y])!=abs(x-y)for x in q for y in q if y-x)])