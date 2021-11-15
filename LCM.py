# #########################
# The world's worst LCM 
# function. Using recursive, 
# curried lambda functions 
# to find the Lowest Common 
# Multiple of a List of 
# integers. To be clear, 
# this is incredibly 
# unpractical and just 
# plain heinous. This is 
# for entertainment 
# purposes only. Don't do 
# this in real life.
#
# Code written for Code 
# Golf (As short as 
# possible), efficiency 
# and entertainment.
# #########################

l=lambda n:l([n[0]*n[1]/(lambda g:lambda a,b:g(g,a,b))(lambda g,a,b:g(g,b,a%b) if b else a)(n[0],n[1])]+n[2:]) if len(n)>1 else n[0]

print(l(list(range(1, 200))))