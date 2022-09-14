# #########################
# Triangular Numbers are a 
# sequence of numbers that 
# can all form a triangle. 
# For example:
# 1 -> *
# 3 -> *
#     * *
# 6 -> *
#     * *
#    * * *
#
# This program finds the xth 
# triangular number with the 
# nth dimension. 
# I.E. t(5, 3) = The number 
# of stars needed to form a 
# 3d triangle (tetrahedron) 
# with side length 5 = 35.
# #########################

t=lambda x,n:(x+n-1)*t(x,n-1)/n if n else 1