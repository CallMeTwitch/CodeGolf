# #########################
# Function to find the sum 
# of all numbers from 1 to 
# X to the power of n.
# #########################

f=lambda x,n:(x+1)*f(x,n-1)-sum([f(q+1,n-1)for q in range(x)])if n>1 else x*(x+1)/2