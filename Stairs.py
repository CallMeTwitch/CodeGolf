# #########################
# The StairCase problem is a 
# very common interview 
# problem. The goal is to print 
# all possible combinations of 
# staircases with total size n 
# with individual stair sizes s.
# Don't do this in an interview 
# unless you don't want the job.
# 
# Code written for Code 
# Golf (As short as 
# possiple), efficiency 
# and entertainment.
# #########################

n=5
s=1,2
f=lambda p=[[]]:f([q+[w]for q in p for w in s if sum(q)+w<=n])+[q for q in p if sum(q)==n]if p else[]
print(f())